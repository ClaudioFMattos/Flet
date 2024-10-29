import flet as ft 

def main(page: ft.Page):
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        'Poppins': 'https://fonts.google.com/specimen/Poppins',
        'Dragon Slayer': 'fonts/Dragon Slayer.otf'
    }

    page.title = 'Curso Flet 360'
    page.theme_mode = 'dark'
    page.bgcolor= ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.padding.symmetric(30, 20) # primeiro eixo y, depois eixo x
    page.window.always_on_top = True
    page.window.height = 600
    page.window.width = 800
    page.window.top = 50
    page.window.left = 283

    t1 = ft.Text(
        value = 'Curso Flet 360 - Programador Aventureiro - Front End com Python!',
        style = ft.TextThemeStyle.HEADLINE_LARGE,
        bgcolor = ft.colors.AMBER_ACCENT_700,
        color = ft.colors.INDIGO_800,
        font_family = 'Poppins',
        weight = ft.FontWeight.W_800,
        italic = False,
        # max_lines = 2,
        # overflow = ft.TextOverflow.ELLIPSIS,
        selectable = True,
        size = 28, 
        text_align = ft.TextAlign.CENTER,
    )

    link_style = ft.TextStyle(
        color = ft.colors.LIGHT_BLUE_400, 
        decoration= ft.TextDecoration.UNDERLINE,
        decoration_color= ft.colors.LIGHT_BLUE_400,
        decoration_thickness= 0.75,
        decoration_style= ft.TextDecorationStyle.SOLID)

    destak_text = ft.TextStyle(
        color = ft.colors.PINK_ACCENT_400, 
        weight = ft.FontWeight.W_700,
        bgcolor = ft.colors.LIGHT_BLUE_400)

    t2 = ft.Text(
        spans = [
            ft.TextSpan(text = 'Texto com link', style = link_style, url = 'https://programadoraventureiro.com'),
            ft.TextSpan(text = ' Continuação do texto... '),
            ft.TextSpan(text = 'Texto em destaque!!!', style = destak_text)
        ],
        size = 24
    )

    page.add(t1, t2)
    page.update()


ft.app(target=main, assets_dir='assets/')