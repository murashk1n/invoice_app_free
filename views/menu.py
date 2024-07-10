import flet as ft
from flet_route import Params, Basket
from flet import *
from views.app_bar import AppBar

def page_menu(page: ft.Page, params: Params, basket: Basket):
    
    btn_customer = ft.OutlinedButton(text='Customers', width=200, on_click=lambda _:page.go('/page_all_customers'))
    btn_invoices = ft.OutlinedButton(text='Invoices', width=200, on_click=lambda _:page.go('/page_all_invoices'))
    btn_services = ft.OutlinedButton(text='Services', width=200, on_click=lambda _:page.go('/page_all_services'))
    btn_my_info = ft.OutlinedButton(text='My info', width=200, on_click=lambda _:page.go('/page_my_info'))

    return ft.View(
        "/page_menu",
        
       controls=[
            AppBar().build(),
            Text("Menu",size=30,weight="bold"),
            ft.Row([
            btn_customer,
            btn_invoices,
            btn_services,
            btn_my_info
            ],alignment=MainAxisAlignment.CENTER
            ),
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )