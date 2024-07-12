import flet as ft
from flet_route import Params, Basket
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar

global_service = []

def get_services():
  return global_service

def page_services(page: ft.Page, params: Params, basket: Basket):
  
    def validate(e):
        if all([service_name.value,service_price.value,service_amount.value]):
            btn_add.disabled = False
        else:
            btn_add.disabled = True
        page.update()   
    
    def save(e):
      if (len(mytable.rows) > 1):
          btn_print.disabled = True
      else:
          btn_print.disabled = False
      page.update()
      # Add new service data to global_service list
      service_id = len(global_service)
      global_service.append({
            'id': service_id,
            'name': service_name.value,
            'price': service_price.value,
            'amount': service_amount.value,
            'description': service_description.value
      })
      
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
		  on_select_changed=lambda e:editindex(
        e.control.cells[0].content.value,
        e.control.cells[1].content.value,
        e.control.cells[2].content.value,
        e.control.cells[3].content.value,
        e.control.cells[4].content.value)
				)
			)
      
		  # THEN BLANK AGAIN THE TEXTFIELD
      service_name.value = ""
      service_price.value = ""
      service_amount.value = ""
      service_description.value = ""
      page.update()
      
    def editindex(id, a,b,c,d):
		  # SET NAME TEXTFIELD TO YOU SELECT THE ROW
      youid.value = int(id)
      service_name.value = a
      service_price.value = b
      service_amount.value = c
      service_description.value = d

		  # HIDE THE ADD NEW BUTTON . AND TRUE OF EDIT AND DELETE BUTTON
      # btn_add.visible = False
      btn_delete.visible = True
      btn_edit.visible = True
      page.update()
      
    def editandsave(e):
		    # Update global_service with edited data
      global_service[youid.value] = {
            'id': youid.value,
            'name': service_name.value,
            'price': service_price.value,
            'amount': service_amount.value,
            'description': service_description.value
      }

      # Update the table row with new data
      row = mytable.rows[youid.value]
      row.cells[1].content = Text(service_name.value)
      row.cells[2].content = Text(service_price.value)
      row.cells[3].content = Text(service_amount.value)
      row.cells[4].content = Text(service_description.value)
      show_snack_bar(e.page, 'Updated!')
    
    def removeindex(e):
      # Remove service from global_service
      global_service.pop(youid.value)
      mytable.rows.pop(youid.value)
      
     # Reassign IDs and update the table and global_service
      for index, service in enumerate(global_service):
          service['id'] = index
          row = mytable.rows[index]
          row.cells[0].content = Text(index)

      show_snack_bar(e.page, 'Deleted!')
      btn_add.visible = True
      btn_delete.visible = False
      btn_edit.visible = False
      page.update()
      
    def print_services(e):
      # Implement the print functionality
      print("Printing services...")
      for service in global_service:
        print(service)
        
    youid = Text("")
    service_name = ft.TextField(label='Name', width=200, on_change=validate)
    service_price = ft.TextField(
        label='Price',
        width=200,
        on_change=validate,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"^\d+([.,]\d{0,2})?$",  # Allow numbers with optional one or two decimal places
            replacement_string="",
        )
    )
    service_amount = ft.TextField(
        label='Amount', 
        width=200,
        on_change=validate, 
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))
    service_description = ft.TextField(label='Description', width=200)
    
    btn_add = OutlinedButton(text="Add", width=200, on_click=save, disabled=True)
    btn_delete = ElevatedButton(text="Delete", bgcolor="red", width=200, on_click=removeindex)
    btn_edit = OutlinedButton(text="Edit", width=200, on_click=editandsave)
    btn_print = OutlinedButton(text="Print", width=200, on_click=print_services, disabled=True)

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
        scroll = "always",
        
        controls = [
            AppBar().build(),
            Text(value='SERVICES', size=30),
            ft.Row([
               service_name,
               service_price,
               service_amount,
               service_description],
                   alignment=ft.MainAxisAlignment.CENTER), 
            ft.Row([
                btn_add,
                btn_edit,
                btn_delete,
                btn_print],
                   alignment=ft.MainAxisAlignment.CENTER),
              mytable                    
              ],
              vertical_alignment=MainAxisAlignment.CENTER,
              horizontal_alignment=CrossAxisAlignment.CENTER,
              spacing=26
            )
    
    