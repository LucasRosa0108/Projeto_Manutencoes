from database.connection import conectar

def get_maquinas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, tipo, funcionando, status FROM maquinas")
    dados = cursor.fetchall()
    conn.close()
    return dados

def create_maquina(nome, tipo, funcionando):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO maquinas (nome, tipo, funcionando) VALUES (?, ?, ?)",
        (nome, tipo, funcionando)
    )
    conn.commit()
    conn.close()

def delete_maquina(id_maquina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM maquinas WHERE id = ?", (id_maquina,))
    conn.commit()
    conn.close()

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

def get_maquinas_preditiva():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, tipo, funcionando, status FROM maquinas WHERE tipo = 'Preditiva'")
    dados = cursor.fetchall()
    conn.close()
    return dados

def create_maquina_preditiva(nome, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO maquinas (nome, tipo, funcionando, status) VALUES (?, 'Preditiva', 1, ?)", (nome, status))
    conn.commit()
    conn.close()

def update_status_maquina(id_maquina, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE maquinas SET status = ? WHERE id = ?", (status, id_maquina))
    conn.commit()
    conn.close()
