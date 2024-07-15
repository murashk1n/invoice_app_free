import flet as ft
from flet_route import Params, Basket
from validate_email import validate_email
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import get_user
import re

global_user = ['','','','','','']

def page_my_info(page: ft.Page, params: Params, basket: Basket):
      
    def save(e):
      iban_regex = r'^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$'
      bic_regex = r'^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?$'
      
      if not re.match(iban_regex, user_iban.value):
        show_snack_bar(e.page, 'Invalid IBAN')
      elif user_email.value is not '' and validate_email(user_email.value) == False:
        show_snack_bar(e.page, 'Wrong email format!')
      elif user_email.value is not '' and not re.match(user_bic.value, bic_regex):
        show_snack_bar(e.page, 'Invalid BIC')
      else:
        show_snack_bar(e.page, 'Saved!')
        get_user(global_user)
        page.go('/page_customer')

    def validate(e):
        if all([user_name.value, user_iban.value]):
            global global_user
            global_user = [user_name.value,user_company.value,user_email.value, user_phone.value, user_iban.value, user_bic.value]
            btn_save.disabled = False
        else:
            btn_save.disabled = True
        page.update()

    user_name = ft.TextField(label='Name', value=global_user[0], width=200, on_change=validate)
    user_company = ft.TextField(label='Company', value=global_user[1], width=200)
    user_email = ft.TextField(label='Email', value=global_user[2], width=200)
    user_phone = ft.TextField(label='Phone', value=global_user[3], width=200, input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9+]",
            replacement_string="",
        ))
    user_iban = ft.TextField(label='IBAN', value=global_user[4], width=200, on_change=validate)
    user_bic = ft.TextField(label='BIC', value=global_user[5], width=200)
    btn_save = ft.OutlinedButton(text='Save', width=200, on_click=save, disabled=True)

    return ft.View(
        "/page_my_info",
        
        controls = [
            AppBar().build(),
            Text(value='MY INFO', size=30),
            ft.Row(
              [
                ft.Column(
                  [
                    user_name,
                    user_email,
                    user_iban,
                  ],
                ),
                ft.Column(
                  [
                    user_company,
                    user_phone,
                    user_bic
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