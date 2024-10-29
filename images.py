import flet as ft 

def main(page: ft.Page):
    page.theme_mode = 'light'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.symmetric(10, 10)
    page.auto_scroll = True



    img = ft.Image(
        src = 'https://images.unsplash.com/photo-1709884732273-c20d3347aa40?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGZyZWUlMjBpbWFnZXN8ZW58MHx8MHx8fDI%3D',
        # border_radius = ft.border_radius.only(top_right=30),
        height = 300,
        width = 450,
        fit = ft.ImageFit.CONTAIN,
        repeat = ft.ImageRepeat.REPEAT
    )

    img2 = ft.Image(
        src = 'images/image2.jpg',
        height = 300,
        width = 450,
        tooltip = 'Amsterdam - Cidade Velha'
        )

    page.add(img, img2)

    page.update()


ft.app(target=main, assets_dir='assets/')