import flet as ft

class VerPantallaCitas(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.title = "Agente aquí sus citas"
        self.page.add(ft.Text("Aquí podrá agendar sus citas", style="headlineSmall"))

    def build(self):
        return ft.Column(
            [
                ft.Text("Agende sus citas aquí", style="headlineLarge"),
            ],
            alignment="center",
            horizontal_alignment="center",
        )