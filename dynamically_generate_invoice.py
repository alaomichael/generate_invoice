from fpdf import FPDF

class InvoicePDF(FPDF):
    def header(self):
        # Company Name and Contact
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Leomax International', ln=True, align='C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, '16, Ire-Akari, Zone A, Road 1, Opp. Nigeria, Wire and Cable, Owode, Apata, Ibadan.', ln=True, align='C')
        self.cell(0, 10, 'Phone: +234 7033680599 | Email: contactleomax@gmail.com', ln=True, align='C')
        self.ln(10)  # Add spacing after header
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# Gather dynamic input
customer_name = input("Enter Customer Name: ")
customer_address = input("Enter Customer Address: ")
invoice_no = input("Enter Invoice Number: ")
invoice_date = input("Enter Invoice Date (dd-mm-yyyy): ")
due_date = input("Enter Due Date (dd-mm-yyyy): ")

items = []
while True:
    description = input("Enter Item Description (or type 'done' to finish): ")
    if description.lower() == 'done':
        break
    quantity = int(input("Enter Quantity: "))
    unit_price = float(input("Enter Unit Price: "))
    total_price = quantity * unit_price
    items.append({"description": description, "quantity": quantity, "unit_price": unit_price, "total": total_price})

# Calculate totals
subtotal = sum(item["total"] for item in items)
tax = 0.0  # You can calculate tax if needed
grand_total = subtotal + tax

# Dynamic payment methods
payment_methods = ["Bank Transfer", "Cash", "Credit Card", "Mobile Money"]
print("\nAvailable Payment Methods:")
for i, method in enumerate(payment_methods, start=1):
    print(f"{i}. {method}")
payment_choice = int(input("Choose Payment Method (enter number): "))
payment_method = payment_methods[payment_choice - 1]

# Create PDF instance
pdf = InvoicePDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Customer Information
pdf.cell(0, 10, "Customer Information:", ln=True, align='L')
pdf.multi_cell(0, 10, f"{customer_name}\n{customer_address}", border=0)
pdf.ln(5)

# Add Invoice Information
pdf.cell(0, 10, "Invoice Information:", ln=True, align='L')
pdf.cell(0, 10, f"Invoice No: {invoice_no}", ln=True)
pdf.cell(0, 10, f"Date: {invoice_date}", ln=True)
pdf.cell(0, 10, f"Due Date: {due_date}", ln=True)
pdf.ln(5)

# Add Item/Service Details
pdf.cell(0, 10, "Items/Services:", ln=True, align='L')
for item in items:
    pdf.multi_cell(0, 10, f"Description: {item['description']}\n"
                          f"Quantity: {item['quantity']} | Unit Price: #{item['unit_price']:.2f} | Total: #{item['total']:.2f}")
    pdf.ln(5)

# Add Total Amount
pdf.cell(0, 10, "Totals:", ln=True, align='L')
pdf.cell(0, 10, f"Subtotal: #{subtotal:.2f}", ln=True)
pdf.cell(0, 10, f"Tax: #{tax:.2f}", ln=True)
pdf.cell(0, 10, f"Grand Total: #{grand_total:.2f}", ln=True)
pdf.ln(5)

# Add Payment Details
pdf.cell(0, 10, "Payment Details:", ln=True, align='L')
pdf.cell(0, 10, f"Payment Method: {payment_method}", ln=True)
pdf.ln(10)

# Output to PDF
output_filename = f"invoice_{invoice_no}.pdf"
pdf.output(output_filename)

print(f"Invoice '{output_filename}' generated successfully!")
