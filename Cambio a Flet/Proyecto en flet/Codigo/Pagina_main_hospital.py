import flet as ft
from flet import FontWeight
from Pantalla_instalaciones import VerPantallaInstalaciones
from Pantalla_personal_hospital import VerPantallaPersonal

def main(page: ft.Page):
    scroll=ft.ScrollMode.ALWAYS,
    page.fonts = {
        "Freeman-Regular": "Fonts/Freeman-Regular.ttf"
    }
    
    def Ir_Agendar_citas(e):
        page.views.clear()
        page.views.append(())
        page.update()
        
    def Ir_Citas_agendadas(e):
        pass
    
    def Ir_conocer_personal_hospital(e):
        page.views.append(VerPantallaPersonal(page))
        page.update()
    
    def Ir_instalaciones_hospital(e):
        page.views.append(VerPantallaInstalaciones(page))
        page.update()
    
    def Ir_conocer_historia_hospital(e):
        pass
    
    page.title = "Página principal del hospital"
    page.window_maximized = True
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LOCAL_HOSPITAL_ROUNDED),
        leading_width=50,
        title=ft.Text("Hospital Fontibón E.S.E", color=ft.colors.BLACK, style=ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor=ft.colors.GREEN,
        actions=[
            ft.Container(
                content=ft.MenuBar(
                    style=ft.MenuStyle(
                    alignment=ft.alignment.top_left,
                    bgcolor=ft.colors.YELLOW),
                    expand=True,
                    controls=[
                        ft.SubmenuButton(
                            content=ft.Text("Conoce más sobre el hospital aquí", color = ft.colors.BLACK, size = 18,
                                style= ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("Conoce nuestro equipo"),
                                    leading=ft.Icon(ft.icons.PERSON),
                                    on_click=Ir_conocer_personal_hospital
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("Conoce nuestras instalaciones"),
                                    leading=ft.Icon(ft.icons.LOCAL_HOSPITAL),
                                    on_click=Ir_instalaciones_hospital
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("Conoce nuestra historia"),
                                    leading=ft.Icon(ft.icons.BOOK),
                                    on_click=Ir_conocer_historia_hospital
                                ),
                            ]
                        )
                    ]
                ),
                padding=10,
                alignment=ft.alignment.center,
            ),
        ]
    )
    
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.ElevatedButton(text="Agende sus citas aquí", on_click=Ir_Agendar_citas),
                            ft.ElevatedButton(text="Consulte sus citas aquí", on_click=Ir_Citas_agendadas),
                            ft.ElevatedButton(text="Otro botón"),
                        ],
                        spacing=15,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK,
                    width=220,
                    height=900,
                    border_radius=0,
                ),
            ]
        )
    )

ft.app(target=main)
