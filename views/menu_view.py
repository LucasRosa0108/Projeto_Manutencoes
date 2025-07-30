import flet as ft

def menu_view(page):
    def ir_para_maquinas(e):
        page.go("/maquinas")

    def ir_para_manutencoes(e):
        page.go("/manutencoes")

    page.views.append(
        ft.View(
            "/menu",
            controls=[
                ft.Text("Menu Principal", size=30),
                ft.Row([
                    ft.ElevatedButton("Máquinas", on_click=ir_para_maquinas),
                    ft.ElevatedButton("Manutenções", on_click=ir_para_manutencoes),
                    ft.ElevatedButton("Sair do Programa", on_click=lambda e: page.window_close()),
                ]),
                ft.Text("Alunos: Lucas Gabriel Rosa Moreira", italic=True)
            ]
        )
    )
    page.update()
