import flet as ft
from controllers.maquina_controller import listar_maquinas_preventiva, adicionar_maquina_preventiva, remover_maquina_preventiva

def manutencao_preventiva_view(page):
    def voltar(e):
        page.go("/manutencoes")

    def exibir_explicacao(e):
        def fechar_dlg(ev):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("O que é manutenção preventiva?"),
            content=ft.Text(
                "Manutenção preventiva é realizada antes que falhas ocorram, com base em tempo ou uso.\n"
                "Serve para evitar paradas não planejadas e prolongar a vida útil das máquinas."
            ),
            actions=[
                ft.TextButton("Fechar", on_click=fechar_dlg)
            ]
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    tabela = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("ID")),
        ft.DataColumn(label=ft.Text("Nome")),
        ft.DataColumn(label=ft.Text("Tipo")),
        ft.DataColumn(label=ft.Text("Funcionando")),
        ft.DataColumn(label=ft.Text("Ações")),
    ], rows=[])

    def carregar_maquinas():
        tabela.rows.clear()
        for maq in listar_maquinas_preventiva():
            tabela.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(maq[0]))),
                    ft.DataCell(ft.Text(maq[1])),
                    ft.DataCell(ft.Text(maq[2])),
                    ft.DataCell(ft.Text("Sim" if maq[3] else "Não")),
                    ft.DataCell(ft.ElevatedButton("Remover", on_click=lambda e, id=maq[0]: remover(id))),
                ])
            )
        page.update()

    def adicionar(e):
        if nome_input.value.strip() == "":
            return
        adicionar_maquina_preventiva(nome_input.value)
        nome_input.value = ""
        carregar_maquinas()

    def remover(id):
        remover_maquina_preventiva(id)
        carregar_maquinas()

    nome_input = ft.TextField(label="Nome da máquina", width=300)

    page.views.append(
        ft.View(
            "/manutencao_preventiva",
            controls=[
                ft.Row([ft.Text("Manutenção Preventiva", size=25, weight="bold")]),
                ft.Row([
                    ft.ElevatedButton("O que é?", on_click=exibir_explicacao),
                    ft.ElevatedButton("Voltar", on_click=voltar)
                ]),
                ft.Row([
                    nome_input,
                    ft.ElevatedButton("Adicionar", on_click=adicionar)
                ]),
                tabela
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.ALWAYS
        )
    )

    carregar_maquinas()
