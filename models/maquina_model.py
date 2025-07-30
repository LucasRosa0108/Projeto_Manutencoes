from database.db import conectar

def listar_maquinas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.id, m.nome, m.status_funcionamento, m.usa_preditiva,
        CASE WHEN p.id IS NOT NULL THEN 'Preventiva' ELSE '' END as preventiva,
        CASE WHEN c.id IS NOT NULL THEN 'Corretiva' ELSE '' END as corretiva,
        pr.status_cor
        FROM maquinas m
        LEFT JOIN manutencao_preventiva p ON m.id = p.maquina_id
        LEFT JOIN manutencao_corretiva c ON m.id = c.maquina_id
        LEFT JOIN manutencao_preditiva pr ON m.id = pr.maquina_id
    """)
    dados = cursor.fetchall()
    conn.close()
    return dados
