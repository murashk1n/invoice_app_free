import flet as ft
from flet import *
from flet_route import Params, Basket
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from db_invoices import mytable, tb, calldb
import sqlite3
conn = sqlite3.connect("invoice.db",check_same_thread=False)

def page_all_invoices(page: ft.Page, params: Params, basket: Basket):
    
    # AND RUN SCRIPT FOR CREATE TABLE WHEN FLET FIRST RUN
	# create_table()
	page.scroll = "auto"

	def showInput(e):
		inputcon.offset = transform.Offset(0,0)
		page.update()

	def hidecon(e):
		inputcon.offset = transform.Offset(2,0)
		page.update()

	def savedata(e):
		try:
			# INPUT TO DATABASE
			c = conn.cursor()
			c.execute("INSERT INTO invoice (customer_id, invoice_date, invoice_bankreference, invoice_subtotal, invoice_tax, invoice_total, invoice_due_date) VALUES(?,?,?,?,?,?,?)",
             (customer_id.value, date.value, bank_reference.value, subtotal.value, tax.value, total.value, due_date.value))
			conn.commit()

			# AND SLIDE RIGHT AGAIN IF FINAL INPUT SUUCESS
			inputcon.offset = transform.Offset(2,0)
   
			customer_id.value = ''
			date.value = ''
			bank_reference.value = ''
			subtotal.value = ''
			tax.value = ''
			total.value = ''
			due_date.value = ''

			# REFRESH TABLE
			tb.rows.clear()
			calldb()
			tb.update()
			show_snack_bar(e.page, 'Saved!')
		except Exception as e:
			print(e)

	# CREATE FIELD FOR INPUT
	customer_id = TextField(label="customer id")
	date = TextField(label="invoice date")
	bank_reference = TextField(label="bank reference")
	subtotal = TextField(label="invoice subtotal")
	tax = TextField(label="invoice tax")
	total = TextField(label="invoice total")
	due_date = TextField(label="due date")


	# CREATE MODAL INPUT FOR ADD NEW DATA 
	inputcon = Card(
		# ADD SLIDE LEFT EFFECT
		offset = transform.Offset(2,0),
		animate_offset = animation.Animation(600,curve="easeIn"),
		elevation=30,
		content=Container(
			content=Column([
				Row([
				Text("Add new invoice",size=20,weight="bold"),
				IconButton(icon="close",icon_size=30,
				on_click=hidecon
					),
					]),
				customer_id,
				date,
				bank_reference,
				subtotal,
                tax,
                total,
                due_date,
				FilledButton("Save",
				on_click=savedata
					)
			])
		)
	)

	return ft.View(
    	"/page_all_invoices",
     	scroll = "always",
        
       	controls=[
        	AppBar().build(),
            Text("INVOICES",size=30,weight="bold"),
			ElevatedButton("Add new invoice", on_click=showInput),
   			ElevatedButton(text='Back', on_click=lambda _:page.go('/page_menu')),
		mytable,
		inputcon 
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )