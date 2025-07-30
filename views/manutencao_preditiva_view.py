import flet as ft
from controllers.maquina_controller import (
    listar_maquinas_preditiva,
    adicionar_maquina_preditiva,
    remover_maquina_preditiva,
    atualizar_status_preditiva
)

def manutencao_preditiva_view(page):
    def voltar(e):
        page.go("/manutencoes")

    def exibir_explicacao(e):
        def fechar(ev):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("O que é manutenção preditiva?"),
            content=ft.Text(
                "Manutenção preditiva monitora continuamente a condição da máquina, "
                "permitindo prever falhas e agir antes que aconteçam."
            ),
            actions=[ft.TextButton("Fechar", on_click=fechar)]
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    # Status color mapping
    STATUS_CORES = {
        "Verde": ft.colors.GREEN_300,
        "Amarelo": ft.colors.YELLOW_700,
        "Vermelho": ft.colors.RED_700,
        "Roxo": ft.colors.PURPLE_700,
        "Azul": ft.colors.BLUE_700,
        "Preto": ft.colors.BLACK,
    }

    tabela = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("ID")),
        ft.DataColumn(label=ft.Text("Nome")),
        ft.DataColumn(label=ft.Text("Status")),
        ft.DataColumn(label=ft.Text("Funcionando")),
        ft.DataColumn(label=ft.Text("Ações")),
    ], rows=[])

    def carregar_maquinas():
        tabela.rows.clear()
        for maq in listar_maquinas_preditiva():
            cor = STATUS_CORES.get(maq[4], ft.colors.GREY)
            tabela.rows.append(
                ft.DataRow(
                    color=cor,
                    cells=[
                        ft.DataCell(ft.Text(str(maq[0]))),
                        ft.DataCell(ft.Text(maq[1])),
                        ft.DataCell(ft.Text(maq[4])),
                        ft.DataCell(ft.Text("Sim" if maq[3] else "Não")),
                        ft.DataCell(
                            ft.Row([
                                ft.ElevatedButton("Remover", on_click=lambda e, id=maq[0]: remover(id)),
                                ft.Dropdown(
                                    width=150,
                                    options=[ft.dropdown.Option(s) for s in STATUS_CORES.keys()],
                                    value=maq[4],
                                    on_change=lambda e, id=maq[0]: mudar_status(id, e.control.value)
                                )
                            ])
                        ),
                    ]
                )
            )
        page.update()

    def adicionar(e):
        if nome_input.value.strip() == "":
            return
        adicionar_maquina_preditiva(nome_input.value, "Verde")  # padrão: Verde
        nome_input.value = ""
        carregar_maquinas()

    def remover(id):
        remover_maquina_preditiva(id)
        carregar_maquinas()

    def mudar_status(id, novo_status):
        atualizar_status_preditiva(id, novo_status)
        carregar_maquinas()

    nome_input = ft.TextField(label="Nome da máquina", width=300)

    page.views.append(
        ft.View(
            "/manutencao_preditiva",
            controls=[
                ft.Row([ft.Text("Manutenção Preditiva", size=25, weight="bold")]),
                ft.Row([
                    ft.ElevatedButton("O que é?", on_click=exibir_explicacao),
                    ft.ElevatedButton("Voltar", on_click=voltar)
                ]),
                ft.Row([
                    nome_input,
                    ft.ElevatedButton("Adicionar", on_click=adicionar)
                ]),
                tabela,
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.ALWAYS
        )
    )

    carregar_maquinas()
