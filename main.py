import flet as ft 

def main(page: ft.Page):
    page.title = 'Curso Flet 360'
    page.theme_mode = 'dark'

    msg5 = ft.Text(value='Curso Flet 360 - Programador Aventureiro', size=48, color=ft.colors.PINK_ACCENT_700)

    msg1 = ft.Text(value='Curso Flet 360 - Programador Aventureiro', size=14, color=ft.colors.AMBER_ACCENT_700)

    msg2 = ft.Text(value='Curso Flet 360 - Programador Aventureiro', size=18, color=ft.colors.LIME_700)

    msg3 = ft.Text(value='Curso Flet 360 - Programador Aventureiro', size=24, color=ft.colors.LIGHT_BLUE_700)

    msg4 = ft.Text(value='Curso Flet 360 - Programador Aventureiro', size=36, color=ft.colors.LIGHT_GREEN_ACCENT_700)

    elements = [
        msg1,
        msg2,
        msg3,
        msg4,
        msg5,
    ]

    page.add(*elements)

ft.app(target=main)


