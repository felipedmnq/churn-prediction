from fpdf import FPDF
from datetime import datetime


width = 210
today = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
pdf = FPDF()
pdf.add_page()

# Header
pdf.image('pdf_images/bank_icon2.png')
pdf.set_font('Arial', 'B', 12)
pdf.cell(0.1, 5, f'{today}')

# Body
pdf.set_font('Arial', 'B', 16)
pdf.cell(0.1, 25, 'Summary:')
pdf.set_font('Arial', 'B', 14)
pdf.cell(0.1, 40, 'A dataa frame with the descrition')



pdf.output('../reports/churn_report.pdf', 'F')