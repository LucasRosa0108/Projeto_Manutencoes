import flet as ft
from controllers.maquina_controller import obter_maquinas, adicionar_maquina, remover_maquina

def maquinas_view(page):
    nome_input = ft.TextField(label="Nome da máquina")
    tipo_input = ft.TextField(label="Tipo de manutenção")
    funcionando_input = ft.Switch(label="Funcionando?", value=True)
    tabela = ft.Column()

    def voltar(e):
        page.go("/menu")

    def carregar_tabela():
        tabela.controls.clear()
        maquinas = obter_maquinas()
        for m in maquinas:
            status = "Sim" if m[3] else "Não"
            tabela.controls.append(
                ft.Row([
                    ft.Text(f"{m[0]}"),
                    ft.Text(f"{m[1]}"),
                    ft.Text(f"{m[2]}"),
                    ft.Text(status),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=m[0]: remover(id))
                ])
            )

    def adicionar(e):
        adicionar_maquina(nome_input.value, tipo_input.value, 1 if funcionando_input.value else 0)
        nome_input.value = ""
        tipo_input.value = ""
        funcionando_input.value = True
        carregar_tabela()
        page.update()

    def remover(maquina_id):
        remover_maquina(maquina_id)
        carregar_tabela()
        page.update()

    carregar_tabela()

    page.views.append(
        ft.View(
            "/maquinas",
            controls=[
                ft.Text("Cadastro de Máquinas", size=25),
                nome_input,
                tipo_input,
                funcionando_input,
                ft.ElevatedButton("Adicionar", on_click=adicionar),
                ft.Text("Lista de Máquinas", size=18),
                tabela,
                ft.ElevatedButton("Voltar", on_click=voltar),
            ]
        )
    )
    page.update()
