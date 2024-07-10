import flet as ft
from flet import *
from flet_route import Routing, path
from views.home import Home
from views.page_all_customers import page_all_customers
from views.page_all_services import page_all_services
from views.page_all_invoices import page_all_invoices
from views.page_invoice_details import page_invoice_details
from views.page_all_companies import page_all_companies 
from views.page_invoice_line import page_invoice_line
from views.menu import page_menu

def main(page: ft.Page):

    app_routes = [
        
        path(url="/", clear= True,view=Home),
        path(url="/page_all_customers",clear= True, view=page_all_customers),
        path(url="/page_all_services",clear= True, view=page_all_services),
        path(url="/page_all_invoices",clear= True, view=page_all_invoices),
        path(url="/page_invoice_details",clear= True, view=page_invoice_details),
        path(url="/page_all_companies",clear= True, view=page_all_companies),
        path(url="/page_invoice_line",clear= True, view=page_invoice_line),
        path(url="/page_menu",clear= True, view=page_menu),
    ]
    
    Routing(page=page, app_routes=app_routes)
    
    page.go(page.route)
    
if __name__ == '__main__':
    ft.app(target=main)
