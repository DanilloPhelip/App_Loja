import flet as ft
from funcoes.Produtos import criar_item_ruffles
from funcoes.Produtos import criar_item_Pipoca_mitoca
from funcoes.Produtos import criar_item_pringles
from funcoes.Produtos import criar_item_mittos
from funcoes.Produtos import criar_item_Halls_preto
from funcoes.Produtos import criar_item_amendoim

def main(page: ft.Page):
    # Lista de funções que criam os itens
    itens_funcoes = [
    ("Pipoca Salgada PopCorn MITOKA Pronta Embalagem 25g", criar_item_Pipoca_mitoca),
    ("Batata Pringles Original 104g", criar_item_pringles),
    ("Salgadinho de Milho MITTO'S Queijo Pacote 35g", criar_item_mittos),
    ("Bala Halls Sabor Extra Forte 28g", criar_item_Halls_preto),
    ("Batata Ruffles Elma Chips Sabor 33g", criar_item_ruffles),
    ("AMENDOIM JAPONES DORI 30G", criar_item_amendoim)
]

    # Função que atualiza os itens conforme a pesquisa
    def filtrar_itens(e):
        palavras = e.control.value.lower().split()
        Conteudo_mix_itens.controls.clear()
        for nome, func in itens_funcoes:
            if any(p in nome.lower() for p in palavras):  # todas as palavras
                Conteudo_mix_itens.controls.append(func())
        Conteudo_mix_itens.update()

    def restaurar_itens(e):
        Conteudo_mix_itens.controls.clear()
        for _, func in itens_funcoes:
            Conteudo_mix_itens.controls.append(func())
        Conteudo_mix_itens.update()


    Barra_pesquisa = ft.TextField(
        prefix_icon=ft.icons.SEARCH,
        hint_text="Digite sua pesquisa...",
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        border_radius=40,
        width=350,
        border_color=ft.colors.WHITE,
        focused_border_color=ft.colors.BLACK,
        height=40,
        text_size=15,
        text_align=ft.TextAlign.LEFT,
        content_padding=10,
        on_change=filtrar_itens,
        on_blur=restaurar_itens  # evento de pesquisa
    )

    Conteudo_mix_itens = ft.Column(
        [func() for _, func in itens_funcoes],
        scroll="auto",
        height=450
    )


    page.add(Barra_pesquisa, Conteudo_mix_itens)

ft.app(target=main)