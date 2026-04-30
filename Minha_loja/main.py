import flet as ft
import asyncio
import qrcode
import io
import base64
from pix_util import gerar_payload_pix
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
    page.bgcolor = "#C3D6FFFF"

    carrinho_itens = []

    # Texto contador
    contador = ft.Text("0", size=12, color=ft.colors.WHITE, weight="bold")

    espaco = ft.Text("   ", size=12)  # texto vazio para espaçamento
    logo = ft.Container(
            content=ft.Image(
                src="logo.png",   # caminho da sua imagem
                width=140,
                fit=ft.ImageFit.CONTAIN,
                scale=2.2
            ))
            

    # Ícone do carrinho com contador sobreposto
    carrinho_icon = ft.Stack([
        ft.Container(
            content=ft.Image(
                src="carrinho_compras.gif",   # caminho da sua imagem
                width=55,
                height=55,
                fit=ft.ImageFit.CONTAIN
            ),
            on_click=lambda e: page.go("/carrinho"),
            border_radius=10
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
        focused_border_color="#7CA3F7C0",
        height=40,
        text_size=15,
        text_align=ft.TextAlign.LEFT,
        content_padding=10,
        on_change=filtrar_itens   # evento de filtro
    )


    Container_pesquisa = ft.Container(
            content=ft.Row([Barra_pesquisa], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.colors.TRANSPARENT,
            padding=3,
            border_radius=20

            )


    # Container superior com título e carrinho
    top_bar = ft.Container(
        content=ft.Row(
            [
                
                logo,
                carrinho_icon
            ],
            alignment="spaceBetween"
        ),
        bgcolor="#3A6F80",
        padding=10,
        height=100,
        border_radius=20,
        margin=ft.margin.all(15)
        
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
    
       
    
    def criar_item_carrinho(item, index, atualizar_contador, atualizar_total, page, carrinho_itens):
        quantidade_text = ft.Text(str(item["quantidade"]), color="#000000", size=14, weight="bold")

        valor = item["preco"] * item["quantidade"]
        subtotal_text = ft.Text(
            value=f"Subtotal: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            size=16,
            color="#36003D",
            weight="bold"
        )

        subtotal_container = ft.Container(
            content=subtotal_text,
            border=ft.border.all(1, "#FF0000"),
            padding=5,
            border_radius=10,
        )

        def atualizar_quantidade(e, delta=0):
            item["quantidade"] = max(1, item["quantidade"] + delta)
            quantidade_text.value = str(item["quantidade"])
            subtotal_text.value = f"Subtotal: R$ {item['preco'] * item['quantidade']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            atualizar_contador()
            atualizar_total()
            page.update()

        def excluir_item(index, atualizar_total, page, carrinho_itens):
            carrinho_itens.pop(index)
            atualizar_contador()

            page.views.clear()
            if carrinho_itens:
                page.views.append(
                    ft.View(
                        "/carrinho",
                        [carrinho_view()],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        bgcolor="#C3D6FFFF"
                    )
                )
            else:
                page.views.append(
                    ft.View(
                        "/carrinho",
                        [
                            ft.Column(
                            [
                                ft.Icon(
                                    name=ft.icons.SHOPPING_CART,
                                    size=80,
                                    color="#FFFFFF"
                                ),
                                ft.Text(
                                    "Seu carrinho está vazio!",
                                    size=20,
                                    weight="bold",
                                    color="#3A6F80"
                                ),
                                ft.ElevatedButton(
                                    "Voltar às compras",
                                    icon=ft.icons.ARROW_BACK,
                                    bgcolor="#3A6F80",
                                    color=ft.colors.WHITE,
                                    on_click=lambda e: (
                                        page.go("/"),
                                        page.update()
                                    )
                                )
                            ],
                            spacing=20,
                            alignment="center",
                            horizontal_alignment="center",
                            expand=True
                        )

                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        bgcolor="#C3D6FFFF"
                    )
                )
            page.update()

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Image(src=item["imagem"], width=80, height=80, border_radius=10),
                    ft.Column([
                        ft.Text(item["nome"], width=200, size=12, weight="bold", color=ft.colors.BLACK),
                        ft.Text(f"Preço: R$ {item['preco']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), size=12, color="#000000", weight="bold"),
                        ft.Row([
                            ft.IconButton(ft.icons.REMOVE, on_click=lambda e: atualizar_quantidade(e, -1), icon_color="#000000"),
                            quantidade_text,
                            ft.IconButton(ft.icons.ADD, on_click=lambda e: atualizar_quantidade(e, +1), icon_color="#000000"),
                        ])
                    ])
                ]),
                ft.Row([
                    subtotal_container,
                    ft.Text("                              "),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color="#FF0000",
                        tooltip="Excluir",
                        on_click=lambda e, idx=index: excluir_item(idx, atualizar_total, page, carrinho_itens)
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
            return ft.Column(
                [
                    ft.Icon(
                        name=ft.icons.SHOPPING_CART,
                        size=80,
                        color=ft.colors.WHITE
                    ),
                    ft.Text(
                        "Carrinho vazio",
                        size=20,
                        weight="bold",
                        color="#3A6F80"
                    ),
                    ft.ElevatedButton(
                        "Voltar às compras",
                        icon=ft.icons.ARROW_BACK,
                        bgcolor="#3A6F80",
                        color=ft.colors.WHITE,
                        on_click=lambda e: (
                            page.go("/"),
                            page.update()
                        )
                    )
                ],
                spacing=20,
                alignment="center",
                horizontal_alignment="center",
                expand=True
            )

            

       # cria o botão com texto vazio
        total_button = ft.ElevatedButton(
            content=ft.Text(
                "Total", 
                size=16, 
                weight="bold", 
                color=ft.colors.WHITE
            ),
            bgcolor=ft.colors.GREEN,
            width=400,
            height=40,
            on_click=lambda e: page.go("/total")
        )

        wrapper = ft.Container(
            content=total_button,
            border_radius=48,
            padding=0,
            border=ft.border.all(2, ft.colors.GREEN),
        )

        async def pulsar():
            while True:
                # Fade in
                for alpha in range(0, 200, 10):
                    wrapper.border = ft.border.all(
                        8,
                        ft.colors.with_opacity(alpha/255, ft.colors.GREEN)
                    )
                    page.update()
                    await asyncio.sleep(0.08)

                # Fade out
                for alpha in range(220, -1, -5):
                    wrapper.border = ft.border.all(
                        8,
                        ft.colors.with_opacity(alpha/240, ft.colors.GREEN)
                    )
                    page.update()
                    await asyncio.sleep(0.01)

        page.run_task(pulsar)

        def atualizar_total():
            total = sum(item["preco"] * item["quantidade"] for item in carrinho_itens)
            total_button.content.value = f"Total: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            # aqui não precisa chamar total_button.update()
            # basta chamar page.update() no final da função
            page.update()

        # monta cada item chamando a função separada
        itens_ui = [
            criar_item_carrinho(item, idx, atualizar_contador, atualizar_total, page, carrinho_itens)
            for idx, item in enumerate(carrinho_itens)
        ]


        atualizar_total()

        return ft.Column([ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/")),
            ft.Text("Carrinho de Compras", size=18, weight="bold", color=ft.colors.WHITE),
            ft.ListView(
                controls=itens_ui,
                expand=True,
                spacing=10,
                padding=10
            ),
            wrapper,   # agora o botão está dentro da página
            
        ], spacing=15, expand=True)



    chave_pix = "bf688789-e586-4123-88b3-9c2bdcf42d43" 

    # Controle de rotas
    def route_change(e):
        page.views.clear()  # sempre limpe as views

        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [home_view()],   # monta a home sempre a partir do estado atual
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor="#C3D6FFFF"
                )
            )

        elif page.route == "/carrinho":
            page.views.append(
                ft.View(
                    "/carrinho",
                    [carrinho_view()],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor="#C3D6FFFF"
                )
            )

       


        elif page.route == "/total":
            try:
                valor = sum(item["preco"] * item["quantidade"] for item in carrinho_itens)
            except Exception:
                valor = 0

            payload = gerar_payload_pix(chave_pix, nome="Danillo", cidade="Manaus", valor=valor)

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=5,
                border=2,
            )
            qr.add_data(payload)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            qr_image = ft.Image(
                src_base64=base64.b64encode(buffer.read()).decode("utf-8"),
                width=250,
                height=250
            )

            # Campo de texto não editável
            copia_cola_field = ft.TextField(
                value=payload,
                read_only=True,          # impede edição
                width=350,
                height=40,
                text_size=14,
                color=ft.colors.BLACK,
                border_color="#C2C2C2",
                bgcolor=ft.colors.WHITE,
                border_radius=15,
                content_padding=10
            )

            # Botão de copiar
            # Botão de copiar com texto
            margem = ft.Text("    ") 
            Text = ft.Text(" Código Pix Copia e Cola:", size=15, color="#000000", weight="bold" ) # margem para separar o botão do campo
            copiar_button = ft.ElevatedButton(
                text="Copiar Código",
                icon=ft.icons.COPY,
                width=150,
                icon_color=ft.colors.BLACK,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                on_click=lambda e: (
                    page.set_clipboard(payload),  # copia para área de transferência
                    setattr(page, "snack_bar", ft.SnackBar(ft.Text("Código copiado!"), open=True)),
                    page.update()
                )
            )


            linha_copiar = ft.Row(
                controls=[Text, copiar_button,  margem],
                alignment="end"   # botão alinhado à direita
            )

            # Colocar lado a lado
            copia_cola_row = ft.Column(
                controls=[ linha_copiar,
                          copia_cola_field
                        ],
                alignment="center"
            )

            Total_a_pagar = ft.TextField(
                value=f"Total a Pagar: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                read_only=True,
                width=350,
                height=43,
                text_size=22,                      
                border_color="#C2C2C2",
                bgcolor="#FFFFFF",                   # fundo mais claro para destacar
                border_radius=15,
                content_padding=0,
                color="#3A6F80",                     # azul mais vibrante
                text_style=ft.TextStyle(
                    weight="bold",                   # negrito
                    shadow=ft.BoxShadow(             # sombra para dar efeito "brilho"
                        spread_radius=1,
                        blur_radius=4,
                        color="#FFFFFF",
                        offset=ft.Offset(1, 1)
                    )
                ),
                text_align=ft.TextAlign.CENTER,
                      # centraliza o texto
            )

            Linha_Total_a_pagar = ft.Row(
                controls=[Total_a_pagar, margem],
                alignment="center")   # centraliza o total   )

            page.views.append(
                ft.View(
                    "/total",
                    [
                        ft.Text("QR Code PIX Gerado", size=20, color="#000000", weight="bold"),
                        qr_image,
                        copia_cola_row,
                        Linha_Total_a_pagar,
                        ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/carrinho"))
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor="#E6FEFFFF"
                )
            )

        page.update()



    # Barra superior com ícone de carrinho e contador
    
    page.on_route_change = route_change
    page.go("/")  # inicia na home

ft.app(target=main)
