import flet as ft
from flet import *
from flet_route import Params, Basket
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from db_customers import mytable, tb, calldb
import sqlite3

conn = sqlite3.connect("invoice.db",check_same_thread=False)

def page_all_customers(page: ft.Page, params: Params, basket: Basket):

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
			c.execute("INSERT INTO customer (firstname,lastname,address,zip,city, phone, email) VALUES(?,?,?,?,?,?,?)",(firstname.value,lastname.value,address.value,zip.value,city.value, phone.value, email.value))
			conn.commit()
			# AND SLIDE RIGHT AGAIN IF FINAL INPUT SUUCESS
			inputcon.offset = transform.Offset(2,0)
   
			firstname.value =''
			lastname.value =''
			address.value =''
			zip.value =''
			city.value =''
			phone.value =''
			email.value =''

			# REFRESH TABLE
			tb.rows.clear()
			calldb()
			tb.update()
			show_snack_bar(e.page, 'Saved!')
		except Exception as e:
			print(e)

	# CREATE FIELD FOR INPUT
	firstname = TextField(label="firstname")
	lastname = TextField(label="lastname")
	address = TextField(label="address")
	zip = ft.TextField(label="zip",input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))
	city = TextField(label="city")
	phone = TextField(label="phone", input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9+]",
            replacement_string="",
        ))
	email = TextField(label="email")

	# CREATE MODAL INPUT FOR ADD NEW DATA 
	inputcon = Card(
		# ADD SLIDE LEFT EFFECT
		offset = transform.Offset(2,0),
		animate_offset = animation.Animation(600,curve="easeIn"),
		elevation=30,
		content=Container(
			content=Column([
				Row([
				Text("Add new customer",size=20,weight="bold"),
				IconButton(icon="close",icon_size=30,
				on_click=hidecon
					),
					]),
				firstname,
				lastname,
				address,
				zip,
				city,
				phone,
				email,
				FilledButton("Save",
				on_click=savedata
				)
			])
		)
	)

	return ft.View(
    	"/page_all_customers",
       	scroll = "always",
        
       	controls=[
            AppBar().build(),
            Text("CUSTOMERS",size=30,weight="bold"),
			ElevatedButton("Add new customer", on_click=showInput),
   			ElevatedButton(text='Back', on_click=lambda _:page.go('/page_menu')),
		mytable,
  		inputcon,
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )