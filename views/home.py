from flet_route import Params, Basket
from flet import *
from views.app_bar import AppBar

def Home(page: Page, params: Params, basket: Basket):
    
    body = Container(
        Stack([
            Column([
                Row([
                    FilledButton("START",
                    style=ButtonStyle(shape=CircleBorder(),padding=30),
                    on_click=lambda _:page.go('/page_menu'),
            )],alignment=MainAxisAlignment.CENTER,) 
            ])
        ])
    )
   
    return View(
        "/",        
       controls=[
            AppBar().build(),
            body
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )