import flet as ft
from views.menu_view import menu_view
from views.maquinas_view import maquinas_view
from views.manutencoes_view import manutencoes_view
from views.manutencao_preventiva_view import manutencao_preventiva_view
from views.manutencao_corretiva_view import manutencao_corretiva_view
from views.manutencao_preditiva_view import manutencao_preditiva_view

def main(page: ft.Page):
    page.title = "Sistema de Manutenção"
    page.window_maximized = True
    page.scroll = ft.ScrollMode.ALWAYS

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            menu_view(page)
        elif page.route == "/maquinas":
            maquinas_view(page)
        elif page.route == "/manutencoes":
            manutencoes_view(page)
        elif page.route == "/manutencao_preventiva":
            manutencao_preventiva_view(page)
        elif page.route == "/manutencao_corretiva":
            manutencao_corretiva_view(page)
        elif page.route == "/manutencao_preditiva":
            manutencao_preditiva_view(page)

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
