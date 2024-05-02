import flet as ft
import database

def main(page: ft.Page):
    text_cedula = ft.TextField(label="Cedula", text_align=ft.TextAlign.CENTER, width=200)
    text_clave = ft.TextField(label="Clave", text_align=ft.TextAlign.CENTER, width=200, password=True)
    register_button = ft.ElevatedButton(text="Crear usuario", width=200, disabled=True)
    
    
    def validate(e: ft.ControlEvent) -> None:
        if all([text_cedula.value, text_clave.value]):
            register_button.disabled = False
        else:
            register_button.disabled = True
            
        page.update()
    
    def submit(e: ft.ControlEvent) -> None:
        database.create_user(text_cedula.value, text_clave.value)
        page.clean()
        
        page.add(
            ft.Text("Bienvenido!")
        )
        
    text_cedula.on_change = validate
    text_clave.on_change = validate
    register_button.on_click = submit
    
    page.add(
        ft.Column([text_cedula, text_clave, register_button])
    )

    
ft.app(target=main)