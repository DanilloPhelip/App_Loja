import flet as ft
from funcoes.fucao_style import estilo_botao
from funcoes.Produtos import criar_item_ruffles
from funcoes.Produtos import criar_item_Pipoca_mitoca
from funcoes.Produtos import criar_item_pringles
from funcoes.Produtos import criar_item_mittos
from funcoes.Produtos import criar_item_Halls_preto
from funcoes.Produtos import criar_item_amendoim
from perfil import perfil_view


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_max_height = 750
    page.window_width = 400
    
    page.bgcolor = "#36003D"
    

    conteudo_area = ft.Container()
    selecionado = {"Todos_": False, "Salgadinhos_": False, "Doces_": False, "Militos_": False}

    def atualizar_estilos():
        btn_Todos_.bgcolor = ft.colors.BLUE_GREY if selecionado["Todos_"] else ft.colors.WHITE
        btn_Todos_.color = ft.colors.WHITE if selecionado["Todos_"] else ft.colors.BLACK
        btn_Salgadinhos_.bgcolor = ft.colors.BLUE_GREY if selecionado["Salgadinhos_"]else ft.colors.WHITE
        btn_Salgadinhos_.color = ft.colors.WHITE if selecionado["Salgadinhos_"] else ft.colors.BLACK
        btn_Doces_.bgcolor = ft.colors.BLUE_GREY if selecionado["Doces_"] else ft.colors.WHITE
        btn_Doces_.color = ft.colors.WHITE if selecionado["Doces_"] else ft.colors.BLACK
        btn_Militos_.bgcolor = ft.colors.BLUE_GREY if selecionado["Militos_"] else ft.colors.WHITE
        btn_Militos_.color = ft.colors.WHITE if selecionado["Militos_"] else ft.colors.BLACK

        btn_Todos_.update()
        btn_Salgadinhos_.update()
        btn_Doces_.update()
        btn_Militos_.update()

    def mostrar_Todos_(e):
        for k in selecionado.keys():
            selecionado[k] = False
        selecionado["Todos_"] = True
        atualizar_estilos()

    def mostrar_Salgadinhos_(e):
        for k in selecionado.keys():
            selecionado[k] = False
        selecionado["Salgadinhos_"] = True
        atualizar_estilos()

    def mostrar_Doces_(e):
        for k in selecionado.keys():
            selecionado[k] = False
        selecionado["Doces_"] = True
        atualizar_estilos()

    def mostrar_Militos_(e):
        for k in selecionado.keys():
            selecionado[k] = False
        selecionado["Militos_"] = True
        atualizar_estilos()


    # cria botões já com estilo
    btn_Todos_ = estilo_botao("Todos", "Todos_", selecionado, on_click=mostrar_Todos_)
    btn_Salgadinhos_ = estilo_botao("Salgadinhos", "Salgadinhos_", selecionado, on_click=mostrar_Salgadinhos_)
    btn_Doces_ = estilo_botao("Doces", "Doces_", selecionado, on_click=mostrar_Doces_)
    btn_Militos_ = estilo_botao("Militos", "Militos_", selecionado, on_click=mostrar_Militos_)

    itens_funcoes = [
        criar_item_Pipoca_mitoca,
        criar_item_pringles,
        criar_item_mittos,
        criar_item_Halls_preto,
        criar_item_ruffles,
        criar_item_amendoim
    ]

    def filtrar_itens(e):
            termo = e.control.value.lower()
            Conteudo_mix_itens.controls.clear()
            for func in itens_funcoes:
                item = func()
                # Aqui você pode definir como comparar: por título, nome, etc.
                if termo in item.controls[0].value.lower():  # supondo que o primeiro controle seja um Text
                    Conteudo_mix_itens.controls.append(item)
            Conteudo_mix_itens.update()

            

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



    Espaco_1 = ft.Text("            ")
    Text_Principal = ft.Image(
        src="personagem.png",   # caminho da imagem dentro da pasta assets
        width=150,                   # largura da imagem
        height=150,                   # altura da imagem
        fit=ft.ImageFit.CONTAIN       # ajusta a imagem sem cortar
    )



    def carrinho_clicado(e):
        e.page.views.clear()  # limpa a tela atual
        e.page.views.append(
            ft.View(
                "/carrinho",
                [
                    ft.Text("Página do Carrinho"),
                    ft.ElevatedButton(
                        "Voltar",
                        on_click=lambda _: voltar_inicio(e.page)
                    )
                ], bgcolor="#36003D"
            )
        )
        e.page.update()


    def voltar_inicio(page: ft.Page):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    conteudo_topo,
                    Conteudo_mix_itens,
                    conteudo_area,
                    ft.ElevatedButton("Ir para Perfil", on_click=lambda e: perfil_view(page))
                ],
                bgcolor="#36003D"
            )
        )
        page.update()

    def main(page: ft.Page):
        voltar_inicio(page)
        
    Text_secundário = ft.GestureDetector(
        content=ft.Image(
            src="carrinho.png",   # caminho da imagem do carrinho dentro da pasta assets
            width=120,
            height=110,
            fit=ft.ImageFit.CONTAIN
        ),
        on_tap=carrinho_clicado
    )



    Espaco_2 = ft.Text("")
    Text_Principal = ft.Image(
        src="personagem.png",   # caminho da imagem dentro da pasta assets
        width=150,                   # largura da imagem
        height=150,                   # altura da imagem
        fit=ft.ImageFit.CONTAIN       # ajusta a imagem sem cortar
    )

    
   # colocar o page.navigation_drawer edef carrinho_clicado(e):,  def voltar_inicio(page): em 
   # arquivos diferente para serem invocados

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            # tela inicial com botão de três pontos

            page.views.append(
                    ft.View(
                        "/",
                        [
                            ft.Column([conteudo_topo, Conteudo_mix_itens, conteudo_area], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        bgcolor="#36003D"
                    )
                )
        
        elif page.route == "/perfil":
                page.views.append(perfil_view())

        page.update()

    
    page.on_route_change = route_change


    # botão de menu (três traços)
    botao_tres_pontos = ft.IconButton(
        icon=ft.icons.MENU_SHARP,          # ícone de três pontos
        icon_color=ft.Colors.WHITE,
        icon_size=30,
        on_click=lambda e: page.go("/perfil")  # chama a função perfil_view
    )

    Container_Text_Principal = ft.Container(
        content=ft.Row([botao_tres_pontos,Espaco_1, Text_Principal, Text_secundário],
         alignment=ft.MainAxisAlignment.START, spacing=10), bgcolor="#5E3264", padding=3)
       
    Container_pesquisa = ft.Container(
        content=ft.Row([Barra_pesquisa], alignment=ft.MainAxisAlignment.CENTER),
         bgcolor="#5E3264",
        padding=3,
        )
    Container_botoes = ft.Container(
        content=ft.Row([btn_Todos_, btn_Salgadinhos_, btn_Doces_, btn_Militos_],
                       alignment=ft.MainAxisAlignment.CENTER,
                       spacing=5,
                       scroll="auto"),
         bgcolor="#5E3264",
        padding=3,
        height=65,
        width=550                    
    )


    conteudo_topo = ft.Column([Container_Text_Principal, 
                            Container_pesquisa, 
                            Container_botoes],
                              alignment=ft.MainAxisAlignment.CENTER,
                              spacing=-2,                    
                              )

    Conteudo_mix_itens = ft.Column([
    criar_item_Pipoca_mitoca(), 
    criar_item_pringles(),
    criar_item_mittos(),
    criar_item_Halls_preto(),
    criar_item_ruffles(),
    criar_item_amendoim()
    ], scroll="auto", height=550)

    page.add(conteudo_topo)
    page.add(Conteudo_mix_itens)
    page.add(conteudo_area)

ft.app(target=main)
#ft.app(target=main, port=24121, assets_dir="assets", view=ft.AppView.WEB_BROWSER, host="0.0.0.0")