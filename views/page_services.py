import flet as ft
from flet_route import Params, Basket
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import get_services

global_service = []

def page_services(page: ft.Page, params: Params, basket: Basket):
  
    def validate(e):
        if all([service_description.value,service_price.value,service_amount.value]):
            get_services(global_service)
            btn_add.disabled = False
        else:
            btn_add.disabled = True
        page.update()   
    
    def add(e):
      btn_add.disabled = True
      if global_service is None:
          btn_generate.disabled = True
      else:
          btn_generate.disabled = False
      page.update()
      # Add new service data to global_service list
      service_id = len(global_service)
      global_service.append({
            'id': service_id,
            'description': service_description.value,
            'price': service_price.value,
            'amount': service_amount.value,
      })
      
      mytable.rows.append(
			DataRow(
			cells=[
				# THIS FOR ID THE YOU TABLE 
				DataCell(Text(len(mytable.rows))),
				DataCell(Text(service_description.value)),
				DataCell(Text(service_price.value)),
				DataCell(Text(service_amount.value)),
			],
			# IF YOU CLIK THIS ROW THEN RUN YOU FUNCTION
			# THIS SCRIPT IS IF CLICK THEN GET THE ID AND NAME OF ROW		
		  on_select_changed=lambda e:editindex(
        e.control.cells[0].content.value,
        e.control.cells[1].content.value,
        e.control.cells[2].content.value,
        e.control.cells[3].content.value)
				)
			)
      
		  # THEN BLANK AGAIN THE TEXTFIELD
      service_description.value = ""
      service_price.value = ""
      service_amount.value = ""

      page.update()
      
    def editindex(id, a,b,c):
		  # SET NAME TEXTFIELD TO YOU SELECT THE ROW
      youid.value = int(id)
      service_description.value = a
      service_price.value = b
      service_amount.value = c

		  # HIDE THE ADD NEW BUTTON . AND TRUE OF EDIT AND DELETE BUTTON
      # btn_add.visible = False
      btn_delete.visible = True
      btn_edit.visible = True
      page.update()
      
    def editandsave(e):
		    # Update global_service with edited data
      global_service[youid.value] = {
            'id': youid.value,
            'description': service_description.value,
            'price': service_price.value,
            'amount': service_amount.value,
      }

      # Update the table row with new data
      row = mytable.rows[youid.value]
      row.cells[1].content = Text(service_description.value)
      row.cells[2].content = Text(service_price.value)
      row.cells[3].content = Text(service_amount.value)

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
        
    youid = Text("")
    service_description = ft.TextField(label='Description', width=200, on_change=validate)
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
        label='Quantity', 
        width=200,
        on_change=validate, 
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))
    
    btn_add = OutlinedButton(text="Add", width=200, on_click=add, disabled=True)
    btn_delete = ElevatedButton(text="Delete", bgcolor="red", width=200, on_click=removeindex)
    btn_edit = OutlinedButton(text="Edit", width=200, on_click=editandsave)
    btn_generate = OutlinedButton(text="Generate PDF", width=200, on_click=lambda _:page.go('/page_generate_pdf'), disabled=True)

    btn_delete.visible = False
    btn_edit.visible = False
    
    # CREATE DATATABLE HERE
    mytable =  DataTable(
		  columns=[
			  DataColumn(Text("id")),
			  DataColumn(Text("description")),
			  DataColumn(Text("price")),
			  DataColumn(Text("quantity")),
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
               service_description,
               service_price,
               service_amount,
               ],
                   alignment=ft.MainAxisAlignment.CENTER), 
            ft.Row([
                btn_add,
                btn_edit,
                btn_delete,
                btn_generate],
                   alignment=ft.MainAxisAlignment.CENTER),
              mytable                    
              ],
              vertical_alignment=MainAxisAlignment.CENTER,
              horizontal_alignment=CrossAxisAlignment.CENTER,
              spacing=26
            )
    
    