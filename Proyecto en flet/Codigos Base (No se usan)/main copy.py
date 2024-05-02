import flet as ft
import database

def main(page: ft.Page):
    page.title = "Registro Hospital"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    text_cedula = ft.TextField(label="Cedula", text_align=ft.TextAlign.CENTER)
    text_clave = ft.TextField(label="Clave", text_align=ft.TextAlign.CENTER, password=True)
    text_nombre = ft.TextField(label="Tu nombre", text_align=ft.TextAlign.CENTER)
    text_apellido = ft.TextField(label="Tu apellido", text_align=ft.TextAlign.CENTER)
    text_sexo = ft.Dropdown(
            width=160,
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Femenino"),
            ],)
    
    register_button = ft.ElevatedButton(text="Crear Usuario", width=200, disabled=True)
    
    def validate(e: ft.ControlEvent) -> None:
        if all([text_cedula.value, text_clave.value, text_nombre, text_apellido]):
            register_button.disabled = False
        else:
            register_button.disabled = True
            
        page.update()
    
    def submit(e: ft.ControlEvent) -> None:
        database.create_user(text_cedula.value, text_clave.value, text_nombre.value, text_apellido.value)
        page.clean()
        
        page.add(
            ft.Text("Bienvenido!")
        )
        
    text_cedula.on_change = validate
    text_clave.on_change = validate
    text_nombre.on_change = validate
    text_apellido.on_change = validate
    register_button.on_click = submit
    
    page.add(
        ft.Column([text_cedula, text_clave, text_nombre, text_apellido, text_sexo, register_button])
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
ft.app(target=main)