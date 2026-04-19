import flet as ft
from perfil import perfil_view   # importa a função do outro arquivo

def main(page: ft.Page):
    page.title = "App com botão de 3 pontos"
    page.bgcolor = ft.Colors.BLUE_GREY_900

    def route_change(e):
        page.views.clear()

        if page.route == "/perfil":
            page.views.append(perfil_view())   # invoca a função importada

        page.update()

    page.on_route_change = route_change

    # Tela inicial com botão de três pontinhos
    page.add(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.MORE_VERT,       # ícone de três pontos
                    icon_color=ft.Colors.WHITE,
                    icon_size=40,
                    on_click=lambda e: page.go("/perfil")  # chama a função perfil_view
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
