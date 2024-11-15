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

# Create PDF instance
pdf = InvoicePDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Customer Information
pdf.cell(0, 10, "Customer Information:", ln=True, align='L')
pdf.multi_cell(0, 10, "Dcns Florence Adegoke\nBeside Ajoke, Opp. Nigeria Wire and Cable Owode, Apata", border=0)
pdf.ln(5)

# Add Invoice Information
pdf.cell(0, 10, "Invoice Information:", ln=True, align='L')
pdf.cell(0, 10, "Invoice No: 0050387", ln=True)
pdf.cell(0, 10, "Date: 14-11-2024", ln=True)
# pdf.cell(0, 10, "Due Date: 14-11-2024", ln=True)
pdf.ln(5)

# Add Item/Service Details
pdf.cell(0, 10, "Items/Services:", ln=True, align='L')
pdf.cell(0, 10, "Description: 60A 12/24V PWM Solar Charge Controller", ln=True)
pdf.cell(0, 10, "Quantity: 1", ln=True)
pdf.cell(0, 10, "Unit Price: #48,000", ln=True)
pdf.cell(0, 10, "Total: #48,000", ln=True)
pdf.ln(5)

# Add Total Amount
pdf.cell(0, 10, "Totals:", ln=True, align='L')
pdf.cell(0, 10, "Grand Total: #48,000", ln=True)
pdf.ln(5)

# Add Payment Details
pdf.cell(0, 10, "Payment Details:", ln=True, align='L')
pdf.cell(0, 10, "Payment Method: Bank Transfer", ln=True)
pdf.ln(10)

# Output to PDF
pdf.output("invoice.pdf")

print("Invoice generated successfully!")
