import flet as ft



#############################################################################################################





def criar_item_Pipoca_mitoca(): 
    Pipoka_mitoka = ft.Image(
            src="pipoca_mitoka.png",   # caminho da imagem do carrinho dentro da pasta assets
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
            ft.Text("R$ 1,25", color="#5E3264", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton("Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#5E3264",
                color=ft.colors.WHITE,
                height=40)
        ], alignment="spaceBetween")
    ], width=200)
        
    Scroll_Descrição_Pipoca = ft.Container(
        content=ft.Row([Pipoka_mitoka, Descrição_pipoca_mitoka]))
    

    Lin_item_pipoca_mitoca = ft.Container(
                content=ft.Row([Scroll_Descrição_Pipoca], spacing=5), 
                width=360, 
                bgcolor=ft.colors.WHITE, 
                border_radius=25,
                height=120

            )

    return Lin_item_pipoca_mitoca 

##############################################################################################################
def criar_item_pringles():

    Batata_Pringles = ft.Image(
                        src="pringles.png",   # caminho da imagem do carrinho dentro da pasta assets
                        width=110,
                        height=115,
                        border_radius=20,
                        fit=ft.ImageFit.COVER
                )
    Descrição_Pringles = ft.Column([
            ft.Text("Batata Pringles Original 104g",
                    color=ft.colors.BLACK, size=12.5, weight="bold"),
            ft.Text("                     "),
            ft.Row([
                ft.Text("R$ 12,99", color="#5E3264", size=25, weight="bold"),
                ft.Text("   "),
                ft.ElevatedButton("Adicionar",
                    icon=ft.icons.ADD,
                    bgcolor="#5E3264",
                    color=ft.colors.WHITE,
                    height=40)
            ], alignment="spaceBetween")
        ], width=200)


    Scroll_Descrição_Pringles= ft.Container(
            content=ft.Row([Batata_Pringles, Descrição_Pringles]))
        


    Lin_item_Pringles = ft.Container(
                content=ft.Row([Scroll_Descrição_Pringles], spacing=5), 
                width=360, 
                bgcolor=ft.colors.WHITE, 
                border_radius=25,
                height=120

                )

    return Lin_item_Pringles

##############################################################################################################

def criar_item_mittos():
    Mittos = ft.Image(
                    src="mittos.png",   # caminho da imagem do carrinho dentro da pasta assets
                    width=110,
                    height=115,
                    border_radius=20,
                    fit=ft.ImageFit.COVER
                )
    Descrição_Mittos= ft.Column([
            ft.Text("Salgadinho de Milho MITTO'S Queijo Pacote 35g",
                    color=ft.colors.BLACK, size=12.5, weight="bold"),
            ft.Text("                     "),
            ft.Row([
                ft.Text("R$ 1,49", color="#5E3264", size=25, weight="bold"),
                ft.Text("       "),
                ft.ElevatedButton("Adicionar",
                    icon=ft.icons.ADD,
                    bgcolor="#5E3264",
                    color=ft.colors.WHITE,
                    height=40)
            ], alignment="spaceBetween")
        ], width=200)


    Scroll_Descrição_mittos = ft.Container(
            content=ft.Row([Mittos, Descrição_Mittos]))
        


    Lin_item_mittos = ft.Container(
                content=ft.Row([Scroll_Descrição_mittos], spacing=5), 
                width=360, 
                bgcolor=ft.colors.WHITE, 
                border_radius=25,
                height=120
            )
    
    return Lin_item_mittos

##############################################################################################################

def criar_item_Halls_preto():
    
    Halls_preto = ft.Image(
                    src="halls_preto.png",   # caminho da imagem do carrinho dentro da pasta assets
                    width=110,
                    height=115,
                    border_radius=20,
                    fit=ft.ImageFit.COVER
            )
    Descrição_Halls = ft.Column([
            ft.Text("Bala Halls Sabor Extra Forte 28g",
                    color=ft.colors.BLACK, size=12.5, weight="bold"),
            ft.Text("                     "),
            ft.Row([
                ft.Text("R$ 3,00", color="#5E3264", size=25, weight="bold"),
                ft.Text("       "),
                ft.ElevatedButton("Adicionar",
                    icon=ft.icons.ADD,
                    bgcolor="#5E3264",
                    color=ft.colors.WHITE,
                    height=40)
            ], alignment="spaceBetween")
        ], width=200)


    Scroll_Descrição_Halls= ft.Container(
            content=ft.Row([Halls_preto, Descrição_Halls]))
        


    Lin_item_Halls = ft.Container(
                content=ft.Row([Scroll_Descrição_Halls], spacing=5), 
                width=360, 
                bgcolor=ft.colors.WHITE, 
                border_radius=25,
                height=120

            )

    return Lin_item_Halls

#############################################################################################################   

def criar_item_ruffles():
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
            ft.Text("R$ 4,49", color="#5E3264", size=25, weight="bold"),
            ft.Text("       "),
            ft.ElevatedButton("Adicionar",
                icon=ft.icons.ADD,
                bgcolor="#5E3264",
                color=ft.colors.WHITE,
                height=40)
        ], alignment="spaceBetween")
    ], width=200)

    Scroll_Descrição_Ruffles = ft.Container(
        content=ft.Row([Batata_Ruffles, Descrição_Ruffles])
    )

    Lin_item_Ruffles = ft.Container(
        content=ft.Row([Scroll_Descrição_Ruffles], spacing=5),
        width=360,
        bgcolor=ft.colors.WHITE,
        border_radius=25,
        height=120
    )

    return Lin_item_Ruffles

#############################################################################################################


def criar_item_amendoim():


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
                ft.Text("R$ 0,95", color="#5E3264", size=25, weight="bold"),
                ft.Text("       "),
                ft.ElevatedButton("Adicionar",
                    icon=ft.icons.ADD,
                    bgcolor="#5E3264",
                    color=ft.colors.WHITE,
                    height=40)
            ], alignment="spaceBetween")
        ], width=200)


    Scroll_Amendoim_Dori= ft.Container(
            content=ft.Row([Batata_Amendoim_Dori, Descrição_Amendoim_Dori]))
        


    Lin_item_Amendoim_Dori = ft.Container(
                content=ft.Row([Scroll_Amendoim_Dori], spacing=5), 
                width=360, 
                bgcolor=ft.colors.WHITE, 
                border_radius=25,
                height=120

                )
    

    return Lin_item_Amendoim_Dori
##############################################################################################################
