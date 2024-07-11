import flet as ft
from flet_route import Params, Basket
from validate_email import validate_email
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import get_user

global_customer = ['','','','']

def page_customer(page: ft.Page, params: Params, basket: Basket):
    
    def save(e):
        if validate_email(customer_email.value) == True:
          show_snack_bar(e.page, 'Saved!')
          global global_customer
          global_customer = [customer_name.value,customer_company.value,customer_email.value, customer_phone.value]
          get_user(global_customer)
          page.go('/page_menu')
        else:
          show_snack_bar(e.page, 'Wrong email format!')  

    def validate(e):
        if all([customer_name.value,customer_company.value,customer_email.value, customer_phone.value]):
            btn_save.disabled = False
        else:
            btn_save.disabled = True
        page.update()

    customer_name = ft.TextField(label='Name', value=global_customer[0], width=200, on_change=validate)
    customer_company = ft.TextField(label='Company', value=global_customer[1], width=200, on_change=validate)
    customer_email = ft.TextField(label='Email', value=global_customer[2], width=200, on_change=validate)
    customer_phone = ft.TextField(label='Phone', value=global_customer[3], width=200, input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9+]",
            replacement_string="",
        ))
    btn_save = ft.OutlinedButton(text='Save', width=200, on_click=save, disabled=True)

    return ft.View(
        "/page_customer",
        
        controls = [
            AppBar().build(),
            Text(value='MY INFO', size=30),
            ft.Row(
              [
                ft.Column(
                  [
                    customer_name,
                    customer_email,
                  ],
                ),
                ft.Column(
                  [
                    customer_company,
                    customer_phone,
                  ],
                ),                    
              ],
              alignment=ft.MainAxisAlignment.CENTER
            ),
            btn_save,
          ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    ) 