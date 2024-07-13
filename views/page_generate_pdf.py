import flet as ft
from flet_route import Params, Basket
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import generate_bill

def page_generate_pdf(page: ft.Page, params: Params, basket: Basket):
    
    def validate():
        if save_file_path.value:
            btn_download.disabled = False
        else:
            btn_download.disabled = True
        page.update()
  
    # Open directory dialog
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else show_snack_bar(e.page, 'Cancelled!')
        save_file_path.update()
        validate()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()
    btn_download = OutlinedButton(text="Download", width=200, on_click=generate_bill, disabled=True)


    # hide all dialogs in overlay
    page.overlay.extend([save_file_dialog])

    return ft.View(
        "/page_generate_pdf",
        
        controls = [
            AppBar().build(),
            Text(value='DOWNLOAD', size=30),
            Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path,
                btn_download
            ],alignment=ft.MainAxisAlignment.CENTER
        ),                    
              ],
              vertical_alignment=MainAxisAlignment.CENTER,
              horizontal_alignment=CrossAxisAlignment.CENTER,
              spacing=26
            )
    
    