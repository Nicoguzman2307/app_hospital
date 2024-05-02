import flet as ft
import database

def main(page: ft.Page):
    
    page.title = "Registro Hospital"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    text_cedula = ft.TextField(label="Cedula", text_align=ft.TextAlign.CENTER)
    text_clave = ft.TextField(label="Clave", text_align=ft.TextAlign.CENTER, password=True)
    register_button = ft.ElevatedButton(text="Iniciar sesion", width=200, disabled=True)
    
    def validate(e: ft.ControlEvent) -> None:
        if all([text_cedula.value, text_clave.value]):
            register_button.disabled = False
        else:
            register_button.disabled = True
            
        page.update()
        
    def submit(e: ft.ControlEvent) -> None:
        cedula = int(text_cedula.value) if text_cedula.value else None
        clave = text_clave.value

        try:
            if database.validate_user(cedula, clave):
                page.clean()
                page.add(ft.Text("¡Inicio de sesión exitoso!"))
            else:
                page.add(ft.Text("Cédula o clave incorrecta. Inténtalo de nuevo."))
        except ValueError as err:
            page.add(ft.Text(f"Error: {err}"))
    
    text_cedula.on_change = validate
    text_clave.on_change = validate
    register_button.on_click = submit

    page.add(
        ft.Column([text_cedula, text_clave, register_button]))
    

ft.app(target=main) #view=ft.WEB_BROWSER