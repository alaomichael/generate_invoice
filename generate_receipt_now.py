# from fpdf import FPDF

# class ReceiptPDF(FPDF):
#     def header(self):
#         # Optional Logo (Uncomment if needed and ensure the path is correct)
#         # try:
#         #     self.image('logo.png', 10, 8, 33)  # Replace with your logo file path
#         # except:
#         #     print("Logo not found. Continuing without logo.")
#         self.set_font('Arial', 'B', 14)
#         self.cell(0, 10, 'Leomax International', ln=True, align='C')
#         self.set_font('Arial', '', 12)
#         self.cell(0, 10, '16, Ire-Akari, Zone A, Road 1, Opp. Nigeria, Wire and Cable, Owode, Apata, Ibadan.', ln=True, align='C')
#         self.cell(0, 10, 'Phone: +234 7033680599 | Email: contactleomax@gmail.com', ln=True, align='C')
#         self.ln(20)

#     def footer(self):
#         self.set_y(-15)
#         self.set_font('Arial', 'I', 8)
#         self.cell(0, 10, f'Page {self.page_no()}', align='C')

# # Input Dynamic Data
# customer_name = input("Enter Customer Name: ")
# customer_address = input("Enter Customer Address: ")
# receipt_no = input("Enter Receipt Number: ")
# payment_date = input("Enter Payment Date (dd-mm-yyyy): ")

# # Dynamic Items
# items = []
# while True:
#     description = input("Enter Item Description (or type 'done' to finish): ")
#     if description.lower() == 'done':
#         break
#     try:
#         quantity = int(input("Enter Quantity: "))
#         unit_price = float(input("Enter Unit Price: "))
#         total_price = quantity * unit_price
#         items.append({"description": description, "quantity": quantity, "unit_price": unit_price, "total": total_price})
#     except ValueError:
#         print("Invalid input! Please enter numeric values for Quantity and Unit Price.")

# # Calculate Total
# total_amount = sum(item["total"] for item in items)

# # Payment Details
# payment_method = input("Enter Payment Method (e.g., Bank Transfer, Cash, Credit Card): ")

# # Create PDF
# pdf = ReceiptPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)

# # Customer Information
# pdf.set_font("Arial", 'B', 12)
# pdf.cell(0, 10, "Receipt for Payment", ln=True, align='C')
# pdf.ln(10)
# pdf.set_font("Arial", '', 12)
# pdf.cell(0, 10, f"Receipt No: {receipt_no}", ln=True)
# pdf.cell(0, 10, f"Date: {payment_date}", ln=True)
# pdf.ln(10)

# # Customer Details
# pdf.set_font("Arial", 'B', 12)
# pdf.cell(0, 10, "Customer Information:", ln=True)
# pdf.set_font("Arial", '', 12)
# pdf.multi_cell(0, 10, f"{customer_name}\n{customer_address}")
# pdf.ln(5)

# # Items Table Header
# pdf.set_fill_color(200, 220, 255)
# pdf.cell(100, 10, "Description", 1, 0, 'C', fill=True)
# pdf.cell(20, 10, "Qty", 1, 0, 'C', fill=True)
# pdf.cell(35, 10, "Unit Price", 1, 0, 'C', fill=True)
# pdf.cell(35, 10, "Total", 1, 1, 'C', fill=True)

# # Items Table Rows
# for item in items:
#     pdf.cell(100, 10, item["description"], 1, 0, 'L')
#     pdf.cell(20, 10, str(item["quantity"]), 1, 0, 'C')
#     pdf.cell(35, 10, f"#{item['unit_price']:.2f}", 1, 0, 'R')
#     pdf.cell(35, 10, f"#{item['total']:.2f}", 1, 1, 'R')

# # Total
# pdf.ln(5)
# pdf.set_font("Arial", 'B', 12)
# pdf.cell(155, 10, "Total Amount:", 0, 0, 'R')
# pdf.set_font("Arial", 'B', 14)
# pdf.cell(35, 10, f"#{total_amount:.2f}", 0, 1, 'R')

# # Payment Method
# pdf.ln(10)
# pdf.set_font("Arial", 'B', 12)
# pdf.cell(0, 10, "Payment Method:", ln=True)
# pdf.set_font("Arial", '', 12)
# pdf.cell(0, 10, f"{payment_method}", ln=True)

# # Output PDF
# output_filename = f"receipt_{receipt_no}.pdf"
# pdf.output(output_filename)

# print(f"Receipt '{output_filename}' generated successfully!")


from fpdf import FPDF

class ReceiptPDF(FPDF):
    def header(self):
        # Optional Logo (Uncomment if needed and ensure the path is correct)
        # try:
        #     self.image('logo.png', 10, 8, 33)  # Replace with your logo file path
        # except:
        #     print("Logo not found. Continuing without logo.")
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
receipt_no = input("Enter Receipt Number: ")
payment_date = input("Enter Payment Date (dd-mm-yyyy): ")

# Dynamic Items
items = []
while True:
    description = input("Enter Item Description (or type 'done' to finish): ")
    if description.lower() == 'done':
        break
    try:
        quantity = int(input("Enter Quantity: "))
        unit_price = float(input("Enter Unit Price: "))
        total_price = quantity * unit_price
        items.append({"description": description, "quantity": quantity, "unit_price": unit_price, "total": total_price})
    except ValueError:
        print("Invalid input! Please enter numeric values for Quantity and Unit Price.")

# Calculate Total
total_amount = sum(item["total"] for item in items)

# Payment Details
payment_method = input("Enter Payment Method (e.g., Bank Transfer, Cash, Credit Card): ")

# Function to format numbers with commas
def format_currency(amount):
    return f"# {amount:,.2f}"

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
    pdf.cell(35, 10, format_currency(item['unit_price']), 1, 0, 'R')
    pdf.cell(35, 10, format_currency(item['total']), 1, 1, 'R')

# Total
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(155, 10, "Total Amount:", 0, 0, 'R')
pdf.set_font("Arial", 'B', 14)
pdf.cell(35, 10, format_currency(total_amount), 0, 1, 'R')

# Payment Method
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Payment Method:", ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"{payment_method}", ln=True)

# Output PDF
output_filename = f"receipt_{receipt_no}.pdf"
pdf.output(output_filename)

print(f"Receipt '{output_filename}' generated successfully!")

