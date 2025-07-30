import flet as ft
import sqlite3

# Função de inicialização do banco
def inicializar_banco():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS maquinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo_manutencao TEXT NOT NULL,
        status TEXT NOT NULL,
        em_preditiva BOOLEAN DEFAULT 0
    )
    """)
    conexao.commit()
    conexao.close()

# Página de máquinas
def pagina_maquinas(page: ft.Page):
    def voltar(e):
        page.views.pop()
        page.update()

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Status")),
            ft.DataColumn(ft.Text("Preditiva")),
        ],
        rows=[]
    )

    # Carregando dados do banco
    con = sqlite3.connect("banco.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM maquinas")
    for row in cur.fetchall():
        table.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(row[0]))),
                ft.DataCell(ft.Text(row[1])),
                ft.DataCell(ft.Text(row[2])),
                ft.DataCell(ft.Text(row[3])),
                ft.DataCell(ft.Text("Sim" if row[4] else "Não")),
            ]
        ))
    con.close()

    page.views.append(
        ft.View(
            "/maquinas",
            [
                ft.Row([ft.Text("Máquinas", size=30), ft.ElevatedButton("Voltar", on_click=voltar)], alignment="spaceBetween"),
                table
            ],
        )
    )
    page.update()

# Página principal
def main(page: ft.Page):
    page.title = "Sistema de Manutenção"
    page.window_full_screen = True  # Tela cheia
    page.window_maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT

    # Alunos do grupo (lado esquerdo)
    nomes_grupo = ft.Column([
        ft.Text("Grupo:", weight="bold"),
        ft.Text("Aluno 1"),
        ft.Text("Aluno 2"),
        ft.Text("Aluno 3"),
    ], alignment="start")

    # Botões laterais (lado direito)
    botoes_menu = ft.Column([
        ft.ElevatedButton("Máquinas", on_click=lambda _: pagina_maquinas(page)),
        ft.ElevatedButton("Manutenções"),
        ft.ElevatedButton("Sobre a Empresa"),
        ft.ElevatedButton("Sair", on_click=lambda _: page.window_close()),
    ], alignment="start")

    # Layout horizontal
    layout = ft.Row([
        ft.Container(nomes_grupo, padding=20, width=200),
        ft.VerticalDivider(width=2),
        ft.Container(botoes_menu, padding=20),
    ])

    page.add(layout)

if __name__ == "__main__":
    inicializar_banco()
    ft.app(target=main)