import flet as ft
from flet import FontWeight
from Pantalla_citas import VerPantallaCitas

def main(page: ft.Page):

    page.fonts = {
        "Freeman-Regular": "Fonts/Freeman-Regular.ttf"
    }
    def Ir_Agendar_citas(e):
        page.views.clear()
        page.views.append(VerPantallaCitas(page))
    def Ir_Citas_agendadas(e):
        page.views.clear()
        page.views.append(())
    def Ir_conocer_personal_hospital(e):
        page.views.clear()
        page.views.append(())
    def Ir_conocer_datos_hospital(e):
        page.views.clear()
        page.views.append(())
    def Ir_conocer_historia_hospital(e):
        page.views.clear()
        page.views.append(())
    
    page.title = "Página principal del hospital"
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LOCAL_HOSPITAL_ROUNDED),
        leading_width=50,
        title=ft.Text("Hospital Fontibón E.S.E", color=ft.colors.BLACK, style = ft.TextStyle(font_family = "Times New Roman"), weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor=ft.colors.GREEN_800,
        actions=[
            ft.SubmenuButton(
                content=ft.Text("Conoce más sobre el hospital aquí", color = ft.colors.BLACK, bgcolor=ft.colors.WHITE, style= ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Conoce nuestro equipo"),
                        leading=ft.Icon(ft.icons.PERSON),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN}),
                        on_click=Ir_conocer_personal_hospital),
                    ft.MenuItemButton(
                        content=ft.Text("Conoce nuestras instalaciones"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN}),
                        on_click=Ir_conocer_datos_hospital
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Conoce nuestra historia"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN}),
                        on_click=Ir_conocer_historia_hospital
                    )
                ]
            ),
        ]
    )
    
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.ElevatedButton(content=ft.Text("Agende sus citas aquí"),on_click=Ir_Agendar_citas),
                            ft.ElevatedButton("Consulte sus citas aquí", on_click=Ir_Citas_agendadas),
                            ft.ElevatedButton("Otro botón"),
                        ],
                        spacing=15,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK,
                    width=220,
                    height=500,
                    border_radius=0,
                ),
            ]
        )
    )


ft.app(target=main)