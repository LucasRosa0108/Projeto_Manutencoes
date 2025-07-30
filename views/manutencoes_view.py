import flet as ft

def manutencoes_view(page):
    def voltar(e):
        page.go("/menu")

    def abrir_preventiva(e):
        page.go("/manutencao_preventiva")

    def abrir_corretiva(e):
        page.go("/manutencao_corretiva")

    def abrir_preditiva(e):
        page.go("/manutencao_preditiva")

    page.views.append(
        ft.View(
            "/manutencoes",
            controls=[
                ft.Text("Tipos de Manutenção", size=25),
                ft.Row([
                    ft.ElevatedButton("Preventiva", on_click=abrir_preventiva),
                    ft.ElevatedButton("Corretiva", on_click=abrir_corretiva),
                    ft.ElevatedButton("Preditiva", on_click=abrir_preditiva),
                ]),
                ft.ElevatedButton("Voltar", on_click=voltar)
            ]
        )
    )
    page.update()
