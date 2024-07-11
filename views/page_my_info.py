import flet as ft
from flet_route import Params, Basket
from validate_email import validate_email
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import get_user

global_user = ['','','','']

def page_my_info(page: ft.Page, params: Params, basket: Basket):
    
    def save(e):
        if validate_email(user_email.value) == True:
          show_snack_bar(e.page, 'Saved!')
          global global_user
          global_user = [user_name.value,user_company.value,user_email.value, user_phone.value]
          get_user(global_user)
          page.go('/page_menu')
        else:
          show_snack_bar(e.page, 'Wrong email format!')  

    def validate(e):
        if all([user_email.value, user_name.value, user_company.value, user_phone.value]):
            btn_save.disabled = False
        else:
            btn_save.disabled = True
        page.update()

    user_name = ft.TextField(label='Name', value=global_user[0], width=200, on_change=validate)
    user_company = ft.TextField(label='Company', value=global_user[1], width=200, on_change=validate)
    user_email = ft.TextField(label='Email', value=global_user[2], width=200, on_change=validate)
    user_phone = ft.TextField(label='Phone', value=global_user[3], width=200, on_change=validate, input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9+]",
            replacement_string="",
        ))
    btn_save = ft.OutlinedButton(text='Save', width=200, on_click=save, disabled=True)

    return ft.View(
        "/page_my_info",
        
        controls = [
            AppBar().build(),
            Text(value='MY INFO', size=30),
            # OutlinedButton(text = "Back to menu",width=200, on_click=lambda _:page.go('/page_menu')),
            ft.Row(
              [
                ft.Column(
                  [
                    user_name,
                    user_email,
                  ],
                ),
                ft.Column(
                  [
                    user_company,
                    user_phone,
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