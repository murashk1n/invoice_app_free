import flet as ft
from flet_route import Params, Basket
from flet import * 
from views.app_bar import AppBar
from util.snack_bar import show_snack_bar
from Bill import get_path, get_invoice, generate_bill
import datetime

def page_generate_pdf(page: ft.Page, params: Params, basket: Basket):
    
  # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        if days_to_pay.value == '':
            days_to_pay.value = 0
        if e.path:
            save_file_path.value = e.path
            get_path(e.path)
            get_invoice([current_date.value, days_to_pay.value, bank_ref.value])
            btn_download.disabled = False
            page.update()
        else:
            show_snack_bar(e.page, 'Cancelled!')
        save_file_path.update()
        
    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()
    
    # hide all dialogs in overlay
    page.overlay.extend([save_file_dialog])
    
    current_date = ft.TextField(
        label='Current date',
        width=200,
        value=datetime.datetime.now().strftime('%d-%m-%Y'),
        disabled=True
    )
    days_to_pay = ft.TextField(
        label='Days to pay',
        width=200,
        value=0,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))

    bank_ref = ft.TextField(
        label='Bank reference', 
        width=200, 
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string="",
        ))
    
    save_btn = OutlinedButton(
                    "Save file",
                    width=200,
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                )
    
    btn_download = ft.OutlinedButton(text='Download', width=200, on_click=generate_bill, disabled=True)

    return ft.View(
        "/page_generate_pdf",
        
        controls = [
            AppBar().build(),
            Text(value='DOWNLOAD', size=30),
            current_date,
            days_to_pay,
            bank_ref,
            save_btn,
            save_file_path,
            btn_download             
            ],
              vertical_alignment=MainAxisAlignment.CENTER,
              horizontal_alignment=CrossAxisAlignment.CENTER,
              spacing=26
            )
    
    