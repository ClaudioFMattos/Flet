import flet as ft

def main(page: ft.Page):
    page.title = 'Curso Flet 360'
    page.bgcolor= ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.symmetric(30, 0) # primeiro eixo y, depois eixo x
    page.window.always_on_top = True
    page.window.height = 400
    # page.window.max_height = 500
    page.window.min_height = 300
    page.window.width = 600
    # page.window.max_width = 800
    page.window.min_width = 300
    page.window.resizable = True
    page.window.title_bar_hidden = False
    page.window.badge_labelfull_screen = False

    page.window.top = 100
    page.window.left = 400
    page.window.movable = False
    # page.window_progress_bar = 0.75

    # def page_resize(e):
    #     print('Tamanho: ', page.window.height, page.window.width)

    # page.on_resized = page_resize

    def window_event(e):
        match e.data:
            case 'focus':
                print('Moveu!')
            case 'minimize':
                print('Minimizou!')
            case _:
                print('Outra ação!', e.data)


        # if e.data == 'maximize':
        #     print('Moveu a página!')
        # elif e.data == 'minimize':
        #     print('Minimizou a página')
        # elif e.data == 'focus':
        #     print('Moveu a página')
        # else:
        #     print('Outra ação!', e.data)


    page.window.on_event = window_event

    # print(page.platform)


    container_1 =  ft.Container(
            ft.Text(value='Curso Flet 360', size=48, weight = ft.FontWeight.W_800, color=ft.colors.AMBER_ACCENT_400), padding=ft.padding.symmetric(50, 25)
        )

    container_2 = ft.Container(ft.Text(value='Programador Aventureiro', size=36, color=ft.colors.BLUE_GREY_800, weight = ft.FontWeight.W_700), bgcolor=ft.colors.AMBER_ACCENT_400, padding=ft.padding.symmetric(50, 25))

    page.add(container_1, container_2)


    page.update()



ft.app(target=main)