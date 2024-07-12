import flet as ft
from flet_route import Params, Basket
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import generate_bill

def page_generate_pdf(page: ft.Page, params: Params, basket: Basket):
    
    def validate():
        if directory_path.value:
            btn_download.disabled = False
        else:
            btn_download.disabled = True
        page.update()
  
    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else show_snack_bar(e.page, 'Cancelled!')
        directory_path.update()
        validate()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()
    btn_download = OutlinedButton(text="Download", width=200, on_click=generate_bill, disabled=True)


    # hide all dialogs in overlay
    page.overlay.extend([get_directory_dialog])

    return ft.View(
        "/page_generate_pdf",
        
        controls = [
            AppBar().build(),
            Text(value='DOWNLOAD', size=30),
            Row(
            [
                ElevatedButton(
                    "Open directory",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
                btn_download
            ],alignment=ft.MainAxisAlignment.CENTER
        ),                    
              ],
              vertical_alignment=MainAxisAlignment.CENTER,
              horizontal_alignment=CrossAxisAlignment.CENTER,
              spacing=26
            )
    
    