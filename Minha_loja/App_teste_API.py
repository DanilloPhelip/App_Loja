import flet as ft
import requests
import asyncio
from funcoes.Produtos import criar_item

async def main(page: ft.Page):
    page.title = "Loja de Snacks"
    page.bgcolor = ft.colors.GREY_100
    page.scroll = "adaptive"

    carrinho = []

    def adicionar_ao_carrinho(nome, preco, imagem):
        carrinho.append({"nome": nome, "preco": preco, "imagem": imagem})
        page.snack_bar = ft.SnackBar(ft.Text(f"{nome} adicionado ao carrinho!"))
        page.snack_bar.open = True
        page.update()

    header = ft.AppBar(
        title=ft.Text("Loja de Snacks", size=20, weight="bold"),
        bgcolor=ft.colors.BLUE_700,
        actions=[ft.IconButton(icon=ft.icons.SHOPPING_CART, tooltip="Carrinho")]
    )

    lista_itens = ft.ListView(expand=True, spacing=10, padding=10)

    footer = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("© 2026 Loja de Snacks", color=ft.colors.BLACK54),
                ft.Text("Feito com Flet", color=ft.colors.BLACK54)
            ],
            alignment="spaceBetween"
        ),
        padding=10
    )

    page.add(header, lista_itens, footer)

    # Função para consultar API e atualizar lista
    def atualizar_produtos():
        try:
            response = requests.get("http://127.0.0.1:5000/produtos")
            produtos = response.json() if response.status_code == 200 else []
        except Exception as e:
            produtos = []
            page.dialog = ft.AlertDialog(
                title=ft.Text("Erro"),
                content=ft.Text(f"Não foi possível carregar os produtos.\n{e}"),
                actions=[ft.TextButton("Fechar", on_click=lambda e: page.dialog.close())]
            )
            page.dialog.open = True

        lista_itens.controls.clear()
        if produtos:
            for produto in produtos:
                lista_itens.controls.append(
                    criar_item(produto["nome"], produto["preco"], produto["imagem"], adicionar_ao_carrinho)
                )
        else:
            lista_itens.controls.append(ft.Text("Nenhum produto disponível", size=16, color=ft.colors.RED))
        page.update()

    # Atualiza imediatamente ao abrir
    atualizar_produtos()

    # Loop assíncrono para atualizar a cada 5 segundos
    async def loop_atualizacao():
        while True:
            atualizar_produtos()
            await asyncio.sleep(5)

    # Inicia o loop paralelo
    asyncio.create_task(loop_atualizacao())

ft.app(target=main)
