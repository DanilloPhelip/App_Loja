import flet as ft

##############################################################################################################
def criar_item_pipoca(adicionar_ao_carrinho):
    Pipoka_mitoka = ft.Image(
        src="pipoca_mitoka.png",
        width=110,
        height=115,
        border_radius=20,
        fit=ft.ImageFit.COVER
    )

    Descrição_pipoca_mitoka = ft.Column([
        ft.Text("Pipoca Salgada PopCorn MITOKA Pronta Embalagem 25g",
                color=ft.colors.BLACK, size=12.5, weight="bold"),
        ft.Text("                     "),
        ft.Row([
            ft.Text("R$ 0,04", color="#3A6F80", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton(
                "Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                height=40,
                on_click=lambda e: adicionar_ao_carrinho(
                    "Pipoca Salgada PopCorn MITOKA Pronta Embalagem 25g",
                    0.04,
                    "pipoca_mitoka.png"
                )
            )
        ], alignment="spaceBetween")
    ], width=200)
        
    return ft.Container(
        content=ft.Row([Pipoka_mitoka, Descrição_pipoca_mitoka]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )

 

##############################################################################################################
def criar_item_pringles(adicionar_ao_carrinho): 
    Batata_Pringles = ft.Image(
                        src="pringles.png",   # caminho da imagem do carrinho dentro da pasta assets
                        width=110,
                        height=115,
                        border_radius=20,
                        fit=ft.ImageFit.COVER)
                
    Descrição_Pringles = ft.Column([
            ft.Text("Batata Pringles Original 104g",
                    color=ft.colors.BLACK, size=12.5, weight="bold"),
            ft.Text("                     "),
            ft.Row([
                ft.Text("R$ 12,99", color="#3A6F80", size=25, weight="bold"),
                ft.Text("   "),
                ft.ElevatedButton("Adicionar",
                    icon=ft.icons.ADD,
                    bgcolor="#3A6F80",
                    color=ft.colors.WHITE,
                    height=40,
                    on_click=lambda e: adicionar_ao_carrinho(
                        "Batata Pringles Original 104g", 12.99,
                        "pringles.png"))
            ], alignment="spaceBetween")
        ], width=200)


    return ft.Container(
        content=ft.Row([Batata_Pringles, Descrição_Pringles]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )


##############################################################################################################

def criar_item_mittos(adicionar_ao_carrinho):
    Mittos = ft.Image(
                    src="mittos.png",   # caminho da imagem do carrinho dentro da pasta assets
                    width=110,
                    height=115,
                    border_radius=20,
                    fit=ft.ImageFit.COVER
                )

    Descrição_pipoca_mitoka = ft.Column([
        ft.Text("Salgadinho de Milho MITTO'S Queijo Pacote 35g",
                color=ft.colors.BLACK, size=12.5, weight="bold"),
        ft.Text("                     "),
        ft.Row([
            ft.Text("R$ 1,49", color="#3A6F80", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton(
                "Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                height=40,
                on_click=lambda e: adicionar_ao_carrinho(
                    "Salgadinho de Milho MITTO'S Queijo Pacote 35g",
                    1.49,
                    "mittos.png"
                )
            )
        ], alignment="spaceBetween")
    ], width=200)
        
    return ft.Container(
        content=ft.Row([Mittos, Descrição_pipoca_mitoka]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )

##############################################################################################################

def criar_item_Halls_preto(adicionar_ao_carrinho):
    Halls_preto = ft.Image(
                    src="halls_preto.png",   # caminho da imagem do carrinho dentro da pasta assets
                    width=110,
                    height=115,
                    border_radius=20,
                    fit=ft.ImageFit.COVER)

    Descrição_Halls = ft.Column([
        ft.Text("Bala Halls Sabor Extra Forte 28g",
                color=ft.colors.BLACK, size=12.5, weight="bold"),
        ft.Text("                     "),
        ft.Row([
            ft.Text("R$ 3,00", color="#3A6F80", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton(
                "Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                height=40,
                on_click=lambda e: adicionar_ao_carrinho(
                    "Bala Halls Sabor Extra Forte 28g",
                    3.00,
                    "halls_preto.png"
                )
            )
        ], alignment="spaceBetween")
    ], width=200)
        
    return ft.Container(
        content=ft.Row([Halls_preto,Descrição_Halls]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )

#############################################################################################################   

def criar_item_ruffles(adicionar_ao_carrinho):
    Batata_Ruffles = ft.Image(
        src="ruffles.png",   # caminho da imagem dentro da pasta assets
        width=110,
        height=115,
        border_radius=20,
        fit=ft.ImageFit.COVER
    )


    Descrição_Ruffles = ft.Column([
        ft.Text("Batata Ruffles Elma Chips Sabor 33g",
                color=ft.colors.BLACK, size=12.5, weight="bold"),
        ft.Text("                     "),
        ft.Row([
            ft.Text("R$ 4,49", color="#3A6F80", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton(
                "Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                height=40,
                on_click=lambda e: adicionar_ao_carrinho(
                    "Batata Ruffles Elma Chips Sabor 33g",
                    4.49,
                    "ruffles.png"
                )
            )
        ], alignment="spaceBetween")
    ], width=200)
        
    return ft.Container(
        content=ft.Row([Batata_Ruffles,Descrição_Ruffles]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )


#############################################################################################################


def criar_item_amendoim(adicionar_ao_carrinho):
    Batata_Amendoim_Dori = ft.Image(
                                src="amendoim_dori.png",   # caminho da imagem do carrinho dentro da pasta assets
                                width=110,
                                height=115,
                                border_radius=20,
                                fit=ft.ImageFit.COVER
                        )

    Descrição_Amendoim_Dori = ft.Column([
        ft.Text("AMENDOIM JAPONES DORI 30G",
                color=ft.colors.BLACK, size=12.5, weight="bold"),
        ft.Text("                     "),
        ft.Row([
            ft.Text("R$ 0,95", color="#3A6F80", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton(
                "Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                height=40,
                on_click=lambda e: adicionar_ao_carrinho(
                    "AMENDOIM JAPONES DORI 30G",
                    0.95,
                    "amendoim_dori.png"
                )
            )
        ], alignment="spaceBetween")
    ], width=200)
        
    return ft.Container(
        content=ft.Row([Batata_Amendoim_Dori,Descrição_Amendoim_Dori]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )

##############################################################################################################

import flet as ft

def criar_item(nome, preco, imagem, adicionar_ao_carrinho):
    produto_img = ft.Image(
        src=imagem,   # caminho da imagem dentro da pasta assets
        width=110,
        height=115,
        border_radius=20,
        fit=ft.ImageFit.COVER
    )

    descricao = ft.Column([
        ft.Text(nome, color=ft.colors.BLACK, size=12.5, weight="bold"),
        ft.Text("                     "),
        ft.Row([
            ft.Text(f"R$ {preco:.2f}", color="#3A6F80", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton(
                "Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#3A6F80",
                color=ft.colors.WHITE,
                height=40,
                on_click=lambda e: adicionar_ao_carrinho(nome, preco, imagem)
            )
        ], alignment="spaceBetween")
    ], width=200)
        
    return ft.Container(
        content=ft.Row([produto_img, descricao]),
        width=360, 
        bgcolor=ft.colors.WHITE, 
        border_radius=25,
        height=120
    )
