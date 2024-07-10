from flet import *
import sqlite3
from util.snack_bar import show_snack_bar

conn = sqlite3.connect('invoice.db',check_same_thread=False)

tb = DataTable(
	columns=[
		DataColumn(Text("Name")),
		DataColumn(Text("Description")),
    	DataColumn(Text("Actions")),
	],
	rows=[]
	)

def showdelete(e):
	try:
		myid = int(e.control.data)
		c = conn.cursor()
		c.execute("DELETE FROM service WHERE id=?", (myid,))
		conn.commit()
		tb.rows.clear()	
		calldb()
		tb.update()
		show_snack_bar(e.page, 'Deleted!')
	except Exception as e:
		print(e)

id_edit = Text()
name_edit = TextField(label="name")
description_edit = TextField(label="description")

def hidedlg(e):
	dlg.visible = False
	dlg.update()

def updateandsave(e):
	try:
		myid = id_edit.value
		c = conn.cursor()
		c.execute("UPDATE service SET name=?, description=? WHERE id=?", (name_edit.value, description_edit.value, myid))
		conn.commit()
		tb.rows.clear()	
		calldb()
		dlg.visible = False
		dlg.update()
		tb.update()
		show_snack_bar(e.page, 'Updated!')
	except Exception as e:
		print(e)

dlg = Container(
	padding=10,
			content=Column([
				Row([
				Text("Edit Form",size=30,weight="bold"),
				IconButton(icon="close",on_click=hidedlg),
					],alignment="spaceBetween"),
				name_edit,
				description_edit,
				ElevatedButton("Update",on_click=updateandsave)
				])
)

def showedit(e):
	data_edit = e.control.data
	id_edit.value = data_edit['id']
	name_edit.value = data_edit['name']
	description_edit.value = data_edit['description']

	dlg.visible = True
	dlg.update()
 
def create_table():
	c = conn.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS service(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		description TEXT)
		""")
	conn.commit()

def calldb():
	create_table()
	c = conn.cursor()
	c.execute("SELECT * FROM service")
	products = c.fetchall()
	if not products == "":
		keys = ['id', 'category_id', 'name', 'description']
		result = [dict(zip(keys, values)) for values in products]
		for x in result:
			tb.rows.append(
				DataRow(
                    cells=[
                        DataCell(Text(x['name'])),
                        DataCell(Text(x['description'])),
                        DataCell(Row([
                        	IconButton(icon="EDIT",icon_color="blue",
                        		data=x,
                        		on_click=showedit
                        	),
                        	IconButton(icon="DELETE",icon_color="red",
                        		data=x['id'],
                        	on_click=showdelete
                        	),
                        ])),
                    ],
                ),

		)

calldb()

dlg.visible = False
mytable = Column([
	dlg,
	Row([tb],scroll="always")
	])