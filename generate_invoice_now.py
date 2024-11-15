from fpdf import FPDF

class InvoicePDF(FPDF):
    def header(self):
        # Optional Logo (Uncomment if needed and ensure the path is correct)
        # try:
        #     self.image('logo.png', 10, 8, 33)  # Replace with your logo file path
        # except:
        #     print("Logo not found. Continuing without logo.")
        # Company Info
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


# Input Dynamic Data
customer_name = input("Enter Customer Name: ")
customer_address = input("Enter Customer Address: ")
invoice_no = input("Enter Invoice Number: ")
invoice_date = input("Enter Invoice Date (dd-mm-yyyy): ")
due_date = input("Enter Due Date (dd-mm-yyyy): ")

# Dynamic Items
items = []
while True:
    description = input("Enter Item Description (or type 'done' to finish): ")
    if description.lower() == 'done' and len(items) > 0:
        break
    elif description.lower() == 'done':
        print("You must add at least one item before finishing.")
        continue
    
    try:
        quantity = int(input("Enter Quantity: "))
        unit_price = float(input("Enter Unit Price: "))
        total_price = quantity * unit_price
        items.append({"description": description, "quantity": quantity, "unit_price": unit_price, "total": total_price})
    except ValueError:
        print("Invalid input! Please enter numeric values for Quantity and Unit Price.")

# Calculate Totals
subtotal = sum(item["total"] for item in items)
try:
    tax_rate = float(input("Enter Tax Rate (e.g., 5 for 5%): "))
except ValueError:
    tax_rate = 0
tax = subtotal * (tax_rate / 100)
grand_total = subtotal + tax

# Dynamic Payment Methods
payment_methods = ["Bank Transfer", "Cash", "Credit Card", "Mobile Money"]
print("\nAvailable Payment Methods:")
for i, method in enumerate(payment_methods, start=1):
    print(f"{i}. {method}")
try:
    payment_choice = int(input("Choose Payment Method (enter number): "))
    payment_method = payment_methods[payment_choice - 1]
except (ValueError, IndexError):
    print("Invalid choice! Defaulting to 'Bank Transfer'.")
    payment_method = "Bank Transfer"

# Create PDF
pdf = InvoicePDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Customer Information
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Customer Information:", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, f"{customer_name}\n{customer_address}")
pdf.ln(5)

# Invoice Information
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Invoice Information:", ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Invoice No: {invoice_no}", ln=True)
pdf.cell(0, 10, f"Date: {invoice_date}", ln=True)
pdf.cell(0, 10, f"Due Date: {due_date}", ln=True)
pdf.ln(5)

# Items Table Header
pdf.set_fill_color(200, 220, 255)
pdf.cell(100, 10, "Description", 1, 0, 'C', fill=True)
pdf.cell(20, 10, "Qty", 1, 0, 'C', fill=True)
pdf.cell(35, 10, "Unit Price", 1, 0, 'C', fill=True)
pdf.cell(35, 10, "Total", 1, 1, 'C', fill=True)

# Items Table Rows
for item in items:
    pdf.cell(100, 10, item["description"], 1, 0, 'L')
    pdf.cell(20, 10, str(item["quantity"]), 1, 0, 'C')
    pdf.cell(35, 10, f"#{item['unit_price']:.2f}", 1, 0, 'R')
    pdf.cell(35, 10, f"#{item['total']:.2f}", 1, 1, 'R')

# Totals
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(155, 10, "Subtotal:", 0, 0, 'R')
pdf.cell(35, 10, f"#{subtotal:.2f}", 0, 1, 'R')
pdf.cell(155, 10, f"Tax ({tax_rate}%):", 0, 0, 'R')
pdf.cell(35, 10, f"#{tax:.2f}", 0, 1, 'R')
pdf.cell(155, 10, "Grand Total:", 0, 0, 'R')
pdf.set_font("Arial", 'B', 14)
pdf.cell(35, 10, f"#{grand_total:.2f}", 0, 1, 'R')

# Payment Details
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Payment Details:", ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Payment Method: {payment_method}", ln=True)

# Output PDF
output_filename = f"invoice_{invoice_no}.pdf"
pdf.output(output_filename)

print(f"Invoice '{output_filename}' generated successfully!")
