import flet as ft

def main(page: ft.Page):
    page.title = 'Curso Flet 360'
    page.bgcolor= ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.symmetric(50, 0) # primeiro eixo y, depois eixo x


    container_1 =  ft.Container(
            ft.Text(value='Curso Flet 360', size=48, weight = ft.FontWeight.W_800, color=ft.colors.AMBER_ACCENT_400), padding=ft.padding.symmetric(50, 25)
        )

    container_2 = ft.Container(ft.Text(value='Programador Aventureiro', size=36, color=ft.colors.BLUE_GREY_800, weight = ft.FontWeight.W_700), bgcolor=ft.colors.AMBER_ACCENT_400, padding=ft.padding.symmetric(50, 25))

    page.add(container_1, container_2)


    page.update()



ft.app(target=main)