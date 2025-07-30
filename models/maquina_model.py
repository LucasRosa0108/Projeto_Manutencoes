from database.connection import conectar

def get_maquinas_por_tipo(tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maquinas WHERE tipo = ?", (tipo,))
    dados = cursor.fetchall()
    conn.close()
    return dados

def create_maquina_tipo(nome, tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO maquinas (nome, tipo, funcionando) VALUES (?, ?, 1)", (nome, tipo))
    conn.commit()
    conn.close()

def delete_maquina_por_id(id_maquina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM maquinas WHERE id = ?", (id_maquina,))
    conn.commit()
    conn.close()
