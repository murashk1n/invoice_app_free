import flet as ft
from flet_route import Params, Basket
from validate_email import validate_email
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import get_user

global_service = ['','','','']

def page_services(page: ft.Page, params: Params, basket: Basket):
    
    def save(e):
      mytable.rows.append(
			DataRow(
			cells=[
				# THIS FOR ID THE YOU TABLE 
				DataCell(Text(len(mytable.rows))),
				DataCell(Text(service_name.value)),
				DataCell(Text(service_price.value)),
				DataCell(Text(service_amount.value)),
				DataCell(Text(service_description.value)),
			],
			# IF YOU CLIK THIS ROW THEN RUN YOU FUNCTION
			# THIS SCRIPT IS IF CLICK THEN GET THE ID AND NAME OF ROW		
		  on_select_changed=lambda e:editindex(e.control.cells[0].content.value,e.control.cells[1].content.value,e.control.cells[2].content.value,e.control.cells[3].content.value,e.control.cells[4].content.value)
				)

			)
		  # THEN BLANK AGAIN THE TEXTFIELD
      service_name.value = ""
      service_price.value = ""
      service_amount.value = ""
      service_description.value = ""
      page.update()
      

          # global global_service
          # global_service = [service_name.value,service_price.value,service_amount.value, service_description.value]
          # get_user(global_service)
 
      
    def editindex(e,a,b,c,d):

		  # SET NAME TEXTFIELD TO YOU SELECT THE ROW
      service_name.value = a
      service_price.value = b
      service_amount.value = c
      service_description.value = d
      youid.value = int(e)

		  # HIDE THE ADD NEW BUTTON . AND TRUE OF EDIT AND DELETE BUTTON
      btn_add.visible = False
      btn_delete.visible = True
      btn_edit.visible = True
      page.update()
      
    def editandsave(e):
		# THIS SCRIPT IS SELECT YOU DATA BEFORE AND
		# CHANGE TO NEW DATA FOR UPDATE IN TEXTFIELD

      mytable.rows[youid.value].cells[1].content = Text(service_name.value)
      mytable.rows[youid.value].cells[2].content = Text(service_price.value)
      mytable.rows[youid.value].cells[3].content = Text(service_amount.value)
      mytable.rows[youid.value].cells[4].content = Text(service_description.value)
      show_snack_bar(e.page, 'Updated!')
    
    def removeindex(e):
      del mytable.rows[youid.value]
      show_snack_bar(e.page, 'Deleted!')
        
    youid = Text("")
    service_name = ft.TextField(label='Name', value=global_service[0], width=200)
    service_price = ft.TextField(label='Price', value=global_service[1], width=200, input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))
    service_amount = ft.TextField(label='Amount', value=global_service[2], width=200, input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))
    service_description = ft.TextField(label='Description', value=global_service[3], width=200)
    
    btn_add = OutlinedButton(text="Add", width=200, on_click=save)
    btn_delete = OutlinedButton(text="Delete", width=200, on_click=removeindex)
    btn_edit = OutlinedButton(text="Edit", width=200, on_click=editandsave)
    
    btn_delete.visible = False
    btn_edit.visible = False
    
    # CREATE DATATABLE HERE
    mytable =  DataTable(
		  columns=[
			  DataColumn(Text("id")),
			  DataColumn(Text("name")),
			  DataColumn(Text("price")),
			  DataColumn(Text("amount")),
			  DataColumn(Text("description")),
		  ],
		#THIS IS YOU ROW OF YOU TABLE
		  rows=[]
		)

    return ft.View(
        "/page_services",
        
        controls = [
            AppBar().build(),
            Text(value='SERVICES', size=30),
            Column([
            ft.Row([
               service_name,
               service_price,
               service_amount,
               service_description]), 
            ft.Row([
                btn_add,
                btn_edit,
                btn_delete]),
              mytable                    
              ])],
              vertical_alignment=MainAxisAlignment.CENTER,
              horizontal_alignment=CrossAxisAlignment.CENTER,
              spacing=26
            )
    
    