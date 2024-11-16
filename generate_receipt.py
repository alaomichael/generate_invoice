import sys
import csv
from fpdf import FPDF
from collections import defaultdict
import traceback

# Retrieve the CSV file path from the command-line arguments
csv_file_path = sys.argv[1]

class ReceiptPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Leomax International', ln=True, align='C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, '16, Ire-Akari, Zone A, Road 1, Opp. Nigeria, Wire and Cable, Owode, Apata, Ibadan.', ln=True, align='C')
        self.cell(0, 10, 'Phone: +234 7033680599 | Email: contactleomax@gmail.com', ln=True, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# Function to format numbers with commas
def format_currency(amount):
    return f"# {amount:,.2f}"

# Read data from CSV
def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    print("Data read from CSV:", data)  # Debugging line to print data
    return data

# Group data by receipt number and fill in missing details
def group_by_receipt(data):
    grouped = defaultdict(list)
    receipt_info = {}
    last_receipt_no = None  # Keep track of the last valid receipt number

    for row in data:
        receipt_no = row.get('receipt_no')

        if receipt_no:  # New receipt, save details
            last_receipt_no = receipt_no
            receipt_info[receipt_no] = {
                "customer_name": row['customer_name'],
                "customer_address": row['customer_address'],
                "payment_date": row['payment_date'],
                "payment_method": row['payment_method']
            }

        # Ensure the row belongs to the last valid receipt
        if last_receipt_no:
            if not receipt_no:  # Fill in missing details
                row['receipt_no'] = last_receipt_no
                row['customer_name'] = receipt_info[last_receipt_no]['customer_name']
                row['customer_address'] = receipt_info[last_receipt_no]['customer_address']
                row['payment_date'] = receipt_info[last_receipt_no]['payment_date']
                row['payment_method'] = receipt_info[last_receipt_no]['payment_method']

            grouped[last_receipt_no].append(row)

    return grouped


# Generate receipt
def generate_receipt(data):
    # Process each receipt
    for receipt_no, items in data.items():
        # Extract the first row for the receipt's details (such as customer, date, payment method)
        first_row = items[0]
        customer_name = first_row['customer_name']
        customer_address = first_row['customer_address']
        payment_date = first_row['payment_date']
        payment_method = first_row['payment_method']

        total_amount = 0
        items_list = []
        for row in items:
            description = row['item_description']
            quantity = int(row['quantity'])
            unit_price = float(row['unit_price'])
            total_price = quantity * unit_price
            items_list.append({"description": description, "quantity": quantity, "unit_price": unit_price, "total": total_price})
            total_amount += total_price

        # Create PDF
        pdf = ReceiptPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Customer Information
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Receipt for Payment", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Receipt No: {receipt_no}", ln=True)
        pdf.cell(0, 10, f"Date: {payment_date}", ln=True)
        pdf.ln(10)

        # Customer Details
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Customer Information:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, f"{customer_name}\n{customer_address}")
        pdf.ln(5)

        # Payment Method
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Payment Method:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, payment_method, ln=True)
        pdf.ln(10)

        # Items Table Header
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(100, 10, "Description", 1, 0, 'C', fill=True)
        pdf.cell(20, 10, "Qty", 1, 0, 'C', fill=True)
        pdf.cell(35, 10, "Unit Price", 1, 0, 'C', fill=True)
        pdf.cell(35, 10, "Total", 1, 1, 'C', fill=True)

        # Items Table Rows
        for item in items_list:
            pdf.cell(100, 10, item["description"], 1, 0, 'L')
            pdf.cell(20, 10, str(item["quantity"]), 1, 0, 'C')
            pdf.cell(35, 10, format_currency(item['unit_price']), 1, 0, 'R')
            pdf.cell(35, 10, format_currency(item['total']), 1, 1, 'R')

        # Total
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(155, 10, "Total Amount:", 0, 0, 'R')
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(35, 10, format_currency(total_amount), 0, 1, 'R')

        # Output PDF
        output_filename = f"receipt_{receipt_no}.pdf"
        pdf.output(output_filename)

        print(f"Receipt '{output_filename}' generated successfully!")

# Main Function to Read CSV, Group by Receipt, and Generate PDF
if __name__ == "__main__":
    # filename = csv_file_path  # "receipt_data.csv"  # CSV file with receipt data
    # data = read_csv(filename)
    # grouped_data = group_by_receipt(data)
    # generate_receipt(grouped_data)
    try:
    # Main execution code
        csv_file_path = sys.argv[1]
        data = read_csv(csv_file_path)
        grouped_data = group_by_receipt(data)
        generate_receipt(grouped_data)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        sys.exit(1)
