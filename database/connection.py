import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return sqlite3.connect(os.getenv("DB_NAME"))

def criar_tabelas():
    con = conectar()
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS maquinas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo_manutencao TEXT,
            funcionando INTEGER DEFAULT 1
        )
    ''')
    con.commit()
    con.close()
