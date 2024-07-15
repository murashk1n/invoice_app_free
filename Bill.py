import flet as ft
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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
        total+=total_price
        services.append([service['description'], service['amount'], f"${float(service['price']):.2f}", f"${float(total_price):.2f}"])

    totalRow = ["Total","", "", total]
    services.append(totalRow)
    
    # Add styles
    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]
    style_heading = styles["Heading1"]

    # Add title
    elements.append(Paragraph("Invoice", style_heading))
    elements.append(Spacer(1, 12))

    # Add company and customer details
    # elements.append(Paragraph(f"My Name: {global_user[0]}", style_normal))
    # elements.append(Paragraph(f"My Company: {global_user[0]}", style_normal))
    # elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Customer Name: {global_customer[0]}", style_normal))
    elements.append(Paragraph(f"Customer Company: {global_customer[1]}", style_normal))
    elements.append(Paragraph(f"Customer e-mail: {global_customer[2]}", style_normal))
    elements.append(Paragraph(f"Customer phone: {global_customer[3]}", style_normal))
    elements.append(Spacer(1, 12))

    # Add the services table
    table = Table(services)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    elements.append(Paragraph(f"Recipient: {global_user[0]}", style_normal))
    elements.append(Paragraph(f"Company: {global_user[1]}", style_normal))
    elements.append(Paragraph(f"e-mail: {global_user[3]}", style_normal))
    elements.append(Paragraph(f"phone: {global_user[4]}", style_normal))
    elements.append(Paragraph(f"IBAN: {global_user[4]}", style_normal))
    elements.append(Paragraph(f"BIC: {global_user[4]}", style_normal))
    elements.append(Spacer(1, 12))

    # Build the PDF
    pdf.build(elements)

    
# def generate_bill_pdf(filename):
#     PDFPSReporte(filename)
    
# class PDFPSReporte:

    # def __init__(self, path):
    #     self.path = path
    #     self.styleSheet = getSampleStyleSheet()
    #     self.elements = []

    #     # colors - Azul turkeza 367AB3
    #     self.colorOhkaGreen0 = Color((45.0/255), (166.0/255), (153.0/255), 1)
    #     self.colorOhkaGreen1 = Color((182.0/255), (227.0/255), (166.0/255), 1)
    #     self.colorOhkaGreen2 = Color((140.0/255), (222.0/255), (192.0/255), 1)
    #     self.colorOhkaBlue0 = Color((54.0/255), (122.0/255), (179.0/255), 1)
    #     self.colorOhkaBlue1 = Color((122.0/255), (180.0/255), (225.0/255), 1)
    #     self.colorOhkaGreenLineas = Color((50.0/255), (140.0/255), (140.0/255), 1)
        
    #     self.PageHeader()
    #     self.tableMaker()
    #     self.PageFooter()
    #     # Build
    #     self.doc = SimpleDocTemplate(path, pagesize=LETTER)
    #     self.doc.multiBuild(self.elements)

    # def PageHeader(self):
    #         get_customer()
            
    #         print(global_services)
            
    #         img = Image('img\logo.png', kind='proportional')
    #         img.drawHeight = 50
    #         img.drawWidth = 50
    #         img.hAlign = 'RIGHT'
    #         self.elements.append(img)
            
    #         psDetalle = ParagraphStyle('Resumen', fontSize=9, leading=14, justifyBreaks=1, alignment=TA_LEFT, justifyLastLine=1)
    #         # name = f"Customer: {global_customer[1]} {global_customer[2]}"
    #         # address = f"Address: {global_customer[3]}"
    #         # phone = f"Phone: {global_customer[6]}"
    #         # email =  f"Email: {global_customer[7]}"
    #         # user =  f"User: {global_user[1]}"
            
    #         # paragraphReportSummary = Paragraph(name, psDetalle)
    #         # self.elements.append(paragraphReportSummary)
    #         # paragraphReportSummary = Paragraph(address, psDetalle)
    #         # self.elements.append(paragraphReportSummary)
    #         # paragraphReportSummary = Paragraph(phone, psDetalle)
    #         # self.elements.append(paragraphReportSummary)
    #         # paragraphReportSummary = Paragraph(email, psDetalle)
    #         # self.elements.append(paragraphReportSummary)
    #         # paragraphReportSummary = Paragraph(user, psDetalle)
    #         # self.elements.append(paragraphReportSummary)

    #         psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_CENTER, borderWidth=3, textColor=self.colorOhkaGreen0)
    #         # text = f"INVOICE {global_customer[0]}"
    #         # paragraphReportHeader = Paragraph(text, psHeaderText)
    #         # self.elements.append(paragraphReportHeader)

    #         spacer = Spacer(10, 10)
    #         self.elements.append(spacer)

    #         d = Drawing(500, 1)
    #         line = Line(-15, 0, 483, 0)
    #         line.strokeColor = self.colorOhkaGreenLineas
    #         line.strokeWidth = 2
    #         d.add(line)
    #         self.elements.append(d)

    #         spacer = Spacer(10, 1)
    #         self.elements.append(spacer)

    #         d = Drawing(500, 1)
    #         line = Line(-15, 0, 483, 0)
    #         line.strokeColor = self.colorOhkaGreenLineas
    #         line.strokeWidth = 0.5
    #         d.add(line)
    #         self.elements.append(d)

    #         spacer = Spacer(10, 22)
    #         self.elements.append(spacer)
            
    # def PageFooter(self):
    #         get_customer()
    #         spacer = Spacer(10, 10)
    #         self.elements.append(spacer)
            
    #         psDetalle = ParagraphStyle('Resumen', fontSize=9, leading=14, justifyBreaks=1, alignment=TA_RIGHT, justifyLastLine=1)
    #         # due_date = f"Due date: {global_customer[0]}"
    #         # bank_reference = f"Bank reference: {global_customer[0]}"
            
    #         # paragraphReportSummary = Paragraph(due_date, psDetalle)
    #         # self.elements.append(paragraphReportSummary)
    #         # paragraphReportSummary = Paragraph(bank_reference, psDetalle)
    #         # self.elements.append(paragraphReportSummary)


    #         spacer = Spacer(10, 10)
    #         self.elements.append(spacer)

    #         d = Drawing(500, 1)
    #         line = Line(-15, 0, 483, 0)
    #         line.strokeColor = self.colorOhkaGreenLineas
    #         line.strokeWidth = 2
    #         d.add(line)
    #         self.elements.append(d)

    #         spacer = Spacer(10, 1)
    #         self.elements.append(spacer)

    #         d = Drawing(500, 1)
    #         line = Line(-15, 0, 483, 0)
    #         line.strokeColor = self.colorOhkaGreenLineas
    #         line.strokeWidth = 0.5
    #         d.add(line)
    #         self.elements.append(d)

    #         spacer = Spacer(10, 22)
    #         self.elements.append(spacer)

    # def tableMaker(self):        
    #     spacer = Spacer(10, 22)
    #     self.elements.append(spacer)
    #     """
    #     Create the line items
    #     """
    #     d = []
    #     textData = ["Line id", "Service", "Quantity", "Price", "Description"]
                
    #     fontSize = 8
    #     centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
    #     for text in textData:
    #         ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
    #         titlesTable = Paragraph(ptext, centered)
    #         d.append(titlesTable)        

    #     data = [d]
    #     lineNum = 1
    #     formattedLineData = []

    #     alignStyle = [ParagraphStyle(name="01", alignment=TA_CENTER),
    #                   ParagraphStyle(name="02", alignment=TA_LEFT),
    #                   ParagraphStyle(name="03", alignment=TA_CENTER),
    #                   ParagraphStyle(name="04", alignment=TA_CENTER),
    #                   ParagraphStyle(name="05", alignment=TA_CENTER)]
        
    #     # c = conn.cursor()
    #     # c.execute("SELECT * FROM invoice_line WHERE invoice_id=?", (global_bill[0], ))
    #     # lines = list(c.fetchall())
        
    #     # for line in lines:
    #     #     print(line)
    #     #     lineData = []
    #     #     lineData.append(str(line[1]))  # Adding invoice line ID
    #     #     lineData.append(str(line[2]))  # Adding product item ID
    #     #     lineData.append(str(line[3]))  # Adding quantity
    #     #     lineData.append(str(line[4]))  # Adding price
    #     #     lineData.append(line[5])  # Adding product description
    
    #     # Now you can proceed to append this lineData to your main data list or perform any other desired operation
    #         # data.append(lineData)

    #     # Row for total
    #     # totalRow = ["Total", "", "", "", global_bill[4]]
    #     # for item in totalRow:
    #     #     ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
    #     #     p = Paragraph(ptext, alignStyle[1])
    #     #     formattedLineData.append(p)
    #     # data.append(formattedLineData)
        
    #     #print(data)
    #     table = Table(data, colWidths=[50, 50, 50, 80, 200])
    #     tStyle = TableStyle([ #('GRID',(0, 0), (-1, -1), 0.5, grey),
    #             ('ALIGN', (0, 0), (0, -1), 'LEFT'),
    #             #('VALIGN', (0, 0), (-1, -1), 'TOP'),
    #             ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
    #             ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
    #             ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
    #             ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
    #             ('SPAN',(0,-1),(-2,-1))
    #             ])
    #     table.setStyle(tStyle)
    #     self.elements.append(table)