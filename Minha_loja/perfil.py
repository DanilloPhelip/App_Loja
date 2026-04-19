import flet as ft

def perfil_view():
    return ft.View(
        "/perfil",
        
        [
            ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_color=ft.Colors.WHITE,
                        icon_size=32,
                        on_click=lambda e: e.page.go("/")  # volta para a tela inicial
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            ft.Column(
                [
                    ft.ElevatedButton("Perfil",
                                    on_click=lambda e: print("Menu clicado"),
                                    bgcolor=ft.colors.with_opacity(0.3, ft.colors.GREY),  # 50% transparente
                                    color=ft.colors.WHITE,
                                    width=1000),
                    ft.ElevatedButton("Histórico", on_click=lambda e: print("Histórico clicado"),
                                    bgcolor=ft.colors.with_opacity(0.3, ft.colors.GREY),
                                    color=ft.colors.WHITE,
                                    width=1000),
                    ft.ElevatedButton("Contato", on_click=lambda e: print("Contato clicado"),
                                    bgcolor=ft.colors.with_opacity(0.3, ft.colors.GREY),
                                    color=ft.colors.WHITE,
                                    width=1000),
                                      

                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        bgcolor= "#36003D"
    )
