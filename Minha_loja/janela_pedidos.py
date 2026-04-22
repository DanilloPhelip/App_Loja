import flet as ft
import locale
from funcoes.Produtos import criar_item_pipoca 
from funcoes.Produtos import criar_item_pringles
from funcoes.Produtos import criar_item_mittos
from funcoes.Produtos import criar_item_Halls_preto
from funcoes.Produtos import criar_item_ruffles
from funcoes.Produtos import criar_item_amendoim

def main(page: ft.Page):
    page.title = "Loja MITOKA"
    page.window.max_height = 850
    page.window.max_width = 400   
    page.bgcolor = "#36003D"

    carrinho_itens = []

    # Texto contador
    contador = ft.Text("0", size=12, color=ft.colors.WHITE, weight="bold")

    # Ícone do carrinho com contador sobreposto
    carrinho_icon = ft.Stack([
            ft.IconButton(
            icon=ft.icons.SHOPPING_CART,
            icon_color=ft.colors.WHITE,
            icon_size=40,   # aumenta o tamanho do ícone
            on_click=lambda e: page.go("/carrinho")
        ),
        ft.Container(
            content=contador,
            bgcolor=ft.colors.RED,
            border_radius=10,
            padding=5,
            right=0,
            top=0
        )
    ])

    # Atualiza o contador do carrinho com a soma das quantidades
        # Atualiza o contador do carrinho com a soma das quantidades
        # Atualiza o contador do carrinho com a soma das quantidades
    def atualizar_contador():
        total_itens = sum(item["quantidade"] for item in carrinho_itens)

        if total_itens > 0:
            contador.value = str(total_itens)   # mostra o número
            contador.visible = True
            contador.bgcolor = ft.colors.RED   # pontinho vermelho ativo
        else:
            contador.value = ""                # não mostra "0"
            contador.visible = False           # esconde o badge
            # se preferir manter o espaço, pode usar:
            # contador.visible = True
            # contador.bgcolor = ft.colors.TRANSPARENT

        page.update()

    # Função para adicionar item ao carrinho sem duplicatas
    def adicionar_ao_carrinho(nome, preco, imagem):
        for item in carrinho_itens:
            if item["nome"] == nome:
                item["quantidade"] += 1
                break
        else:
            carrinho_itens.append({
                "nome": nome,
                "preco": preco,
                "imagem": imagem,
                "quantidade": 1
            })
        atualizar_contador()


        # Lista completa de itens
    todos_itens = [
        criar_item_pipoca(adicionar_ao_carrinho),
        criar_item_pringles(adicionar_ao_carrinho),
        criar_item_mittos(adicionar_ao_carrinho),
        criar_item_Halls_preto(adicionar_ao_carrinho),
        criar_item_ruffles(adicionar_ao_carrinho),
        criar_item_amendoim(adicionar_ao_carrinho)
    ]

    # ListView que será atualizado
    Conteudo_mix_itens = ft.ListView(
        controls=todos_itens,
        expand=True,
        spacing=5,
        padding=5
    )

    # Função de filtro
    def filtrar_itens(e):
        termo = Barra_pesquisa.value.lower()
        Conteudo_mix_itens.controls = [
            item for item in todos_itens
            if termo in item.content.controls[1].controls[0].value.lower()
        ]
        page.update()

    # Barra de pesquisa com evento
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
        on_change=filtrar_itens   # evento de filtro
    )


    Container_pesquisa = ft.Container(
            content=ft.Row([Barra_pesquisa], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor="#5E3264",
            padding=3,
            )


    # Container superior com título e carrinho
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Text("Loja MITOKA", size=20, weight="bold", color=ft.colors.WHITE),
                carrinho_icon
            ],
            alignment="spaceBetween"
        ),
        bgcolor="#5E3264",
        padding=10,
       height=100,
        
    )
          # Área dos itens com scroll
    Conteudo_mix_itens = ft.ListView(
        controls=[
            criar_item_pipoca(adicionar_ao_carrinho), 
            criar_item_pringles(adicionar_ao_carrinho),
            criar_item_mittos(adicionar_ao_carrinho),
            criar_item_Halls_preto(adicionar_ao_carrinho),
            criar_item_ruffles(adicionar_ao_carrinho),
           criar_item_amendoim(adicionar_ao_carrinho)
        ],
        expand=True,        # ocupa todo o espaço disponível
        spacing=5,
        padding=5
    )

    # Página inicial
    def home_view():
        return ft.Column(
            [
                top_bar,             # container superior fixo
                Container_pesquisa,  # pesquisa fixa
                Conteudo_mix_itens   # somente os itens rolam
            ],
            spacing=0,
            expand=True
        )
    
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    # Função para formatar moeda
    def formatar_moeda(valor):
        return locale.currency(valor, grouping=True)
    
    
    # Página do carrinho com scroll, quantidade e soma
    # Função que monta cada item do carrinho
    def criar_item_carrinho(item, atualizar_contador, atualizar_total, page, carrinho_itens):
        quantidade_text = ft.Text(str(item["quantidade"]), color="#000000", size=14, weight="bold")
       # Criação inicial
        valor = item["preco"] * item["quantidade"]
        subtotal_text = ft.Text(
            value=f"Subtotal: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            size=16,
            color="#63C74F",
            weight="bold"
        )

        subtotal_container = ft.Container(
            content=subtotal_text,
            border=ft.border.all(1, "black"),  # borda preta
            padding=5,
            border_radius=20
        )

          # aqui sim aparece a borda
        def atualizar_quantidade(e, delta=0):
            item["quantidade"] = max(1, item["quantidade"] + delta)
            quantidade_text.value = str(item["quantidade"])
            subtotal_text.value = f"Subtotal: R$ {item['preco'] * item['quantidade']:.2f}"
            atualizar_contador()
            atualizar_total()
            page.update()


        def excluir_item(e):
            if item in carrinho_itens:
                carrinho_itens.remove(item)
            atualizar_contador()
            atualizar_total()
            page.controls.clear()
            page.add(carrinho_view())
            page.update()

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Image(src=item["imagem"], width=80, height=80, border_radius=10),
                    ft.Column([
                        ft.Text(item["nome"], width=200, size=12, weight="bold", color=ft.colors.BLACK),
                        ft.Text(f"Preço: R$ {item['preco']:.2f}", size=12, color="#000000", weight="bold"),
                        ft.Row([
                            ft.IconButton(ft.icons.REMOVE, on_click=lambda e: atualizar_quantidade(e, -1), icon_color="#000000"),
                            quantidade_text,
                            ft.IconButton(ft.icons.ADD, on_click=lambda e: atualizar_quantidade(e, +1), icon_color="#000000"),
                            
                        ])
                    ])
                ]),
                ft.Row([subtotal_container,
                    ft.Text("                              "),
                    ft.IconButton(
                        ft.icons.DELETE,
                        tooltip="Excluir",
                        on_click=excluir_item,
                        icon_color="#FF0000"
                    )
                ], alignment="end")
            ]),
            bgcolor=ft.colors.WHITE,
            border_radius=15,
            padding=10,
            margin=0,
            width=150
        )

    # Página do carrinho
    def carrinho_view():
        if not carrinho_itens:
            return ft.Column([
                ft.Text("Carrinho vazio", size=16, color=ft.colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/"))
            ], spacing=15, expand=True)

        total_text = ft.Text("", size=16, weight="bold", color=ft.colors.WHITE)

        def atualizar_total():
            total = sum(item["preco"] * item["quantidade"] for item in carrinho_itens)
            total_text.value = f"Total: R$ {total:.2f}"

        # monta cada item chamando a função separada
        itens_ui = [criar_item_carrinho(item, atualizar_contador, atualizar_total, page, carrinho_itens) for item in carrinho_itens]

        atualizar_total()

        return ft.Column([
            ft.Text("Carrinho de Compras", size=18, weight="bold", color=ft.colors.WHITE),
            ft.ListView(
                controls=itens_ui,
                expand=True,
                spacing=10,
                padding=10
            ),
            total_text,
            ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/"))
        ], spacing=15, expand=True)

        
    # Controle de rotas
    def route_change(e):
        page.controls.clear()
        if page.route == "/":
            page.add(home_view())
        elif page.route == "/carrinho":
            page.add(carrinho_view())
        page.update()

    # Barra superior com ícone de carrinho e contador
    
    page.on_route_change = route_change
    page.go("/")  # inicia na home

ft.app(target=main)
