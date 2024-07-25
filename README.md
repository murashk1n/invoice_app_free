# Invoice_App
[Python](https://www.python.org/)
[Flet](https://flet.dev/)

## User Input Interface:

### You can choose dark or light theme

### Customer Details: Name(required), Company, Address
### Recipient Details: Name(required), Company, Email(validated), Phone(validated), IBAN(required, validated), BIC(validated)
### Invoice Details: Invoice Number, Invoice Date, Due Date, Bank Reference
### Service Details: Description(required), Quantity(required, validated), Unit Price(required, validated), Total Price (calculated automatically)

## This is a simple invoicing application. The user enters data and generates an invoice in PDF.

# How to run

### Download [Visual Studio Code](https://code.visualstudio.com/)

```
git clone https://github.com/murashk1n/invoice_app_free.git
```

### Create virtual environment
https://docs.python.org/3/library/venv.html

### Install all requirements:
```
pip install -r requirements.txt
```
### Run
#### Press Start

<p align="center" border="none">
  <img alt="Home page" src="readme_img\\run.png" align="center">
</p>

### To generate an invoice, you need to enter own data and customer data

<p align="center" border="none">
  <img alt="My Info" src="readme_img\\myinfo.png" align="center">
</p>

<p align="center" border="none">
  <img alt="Invoice page" src="readme_img\\customer.png" align="center">
</p>

### then fill the invoice data, choose the place to download and click download

<p align="center" border="none">
  <img alt="download" src="readme_img\\invoice.png" align="center">
</p>

### file will be downloaded to the choosen folder

<p align="center" border="none">
  <img alt="pdf" src="readme_img\\bill.png" align="center">
</p>