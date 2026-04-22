import flet as ft

def estilo_botao(texto, chave, selecionado, on_click=None):
    cor_fundo = ft.colors.BLUE_GREY if selecionado[chave] else ft.colors.WHITE
    cor_texto = ft.colors.WHITE if selecionado[chave] else ft.colors.BLACK

    return ft.ElevatedButton(
        texto,
        bgcolor=cor_fundo,
        color=cor_texto,
        height=40,
        width=100,
        on_click=on_click,
    )