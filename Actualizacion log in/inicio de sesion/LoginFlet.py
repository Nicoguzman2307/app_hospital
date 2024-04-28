import flet as ft

conteiner = ft.Container(
    border_radius=20,
    width=1000,
    height=1000,
    gradient= ft.LinearGradient([
        ft.colors.PURPLE,
        ft.colors.PINK,
        ft.colors.RED])




)


def main(page: ft.Page):
    page.add(conteiner)

ft.app(target=main)