import flet as ft
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from datetime import datetime, timedelta

global_services = []
global_customer = []
global_user = []
global_path = ''
global_invoice = []

def get_path(path):
    global global_path
    global_path = path
    
def get_invoice(invoice):
    global global_invoice
    global_invoice = invoice
    
def get_customer(customer):
    global global_customer
    global_customer = customer
    
def get_user(user):
    global global_user
    global_user = user
    
def get_services(services):
    global global_services
    global_services = services
   
def generate_bill(e):
    page = e.page
    page.snack_bar = ft.SnackBar(ft.Text('Successful download!'))
    page.snack_bar.open = True
    generate_bill_pdf(global_path)
    page.update()
    
def generate_bill_pdf(filename):
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    total = 0
    
    # Convert global_service list to table data format
    services = [["Description", "Quantity", "Unit Price", "Total"]]
    for service in global_services:
        total_price = float(service['price']) * int(service['amount'])
        total += total_price
        services.append([service['description'], service['amount'], f"{float(service['price']):.2f}", f"{float(total_price):.2f}"])

    totalRow = ["Total", "", "", f"{total:.2f}"]
    services.append(totalRow)
    
    # Add styles
    style_h_L = ParagraphStyle('Resumen', fontSize=15, leading=14, justifyBreaks=1, alignment=TA_LEFT, justifyLastLine=1)
    style_h_R = ParagraphStyle('Resumen', fontSize=15, leading=14, justifyBreaks=1, alignment=TA_RIGHT, justifyLastLine=1)
    style_head = ParagraphStyle('Resumen', fontSize=25, leading=14, justifyBreaks=1, alignment=TA_CENTER, justifyLastLine=1)
    style_right = ParagraphStyle('Resumen', alignment=TA_RIGHT)
    style_left = ParagraphStyle('Resumen', alignment=TA_LEFT)

    # Add header
    elements.append(Paragraph("INVOICE", style_head))
    elements.append(Spacer(1, 30))

    # Add company and customer details
    elements.append(Paragraph(f"Date: {global_invoice[0]}", style_h_L))
    elements.append(Spacer(1, 15))
    elements.append(Paragraph(f"Customer:", style_h_L))
    elements.append(Spacer(1, 15))
    elements.append(Paragraph(f"Name: {global_customer[0]}", style_left))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Company: {global_customer[1]}", style_left))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"E-mail: {global_customer[2]}", style_left))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Phone: {global_customer[3]}", style_left))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Address: {global_customer[4]}", style_left))
    elements.append(Spacer(1, 12))

    # Add the services table
    table = Table(services, colWidths=[200, 100, 100, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 30))
    
    delta = int(global_invoice[1])
    due_date = datetime.now() + timedelta(days=delta)
    # Add recipient details table
    recipient_data = [
        ["IBAN", global_user[4]],
        ["BIC", global_user[5]],
        ["Due date", due_date.strftime('%d-%m-%Y')],
        ["Bank reference", global_invoice[2]],
        ["Total", f"{total:.2f}"],
    ]
    recipient_table = Table(recipient_data, colWidths=[100, 200])
    recipient_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
    ]))
    elements.append(recipient_table)
    elements.append(Spacer(1, 30))
    
    elements.append(Paragraph(f"Recipient: ", style_h_R))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Name: {global_user[0]}", style_right))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Company: {global_user[1]}", style_right))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"E-mail: {global_user[2]}", style_right))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Phone: {global_user[3]}", style_right))
    
    # Add footer
    elements.append(Paragraph("Thank you for your business!", style_h_L))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Please make checks payable to {global_user[1]}", style_h_L))


    # Build the PDF
    pdf.build(elements)
