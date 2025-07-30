import sqlite3
import os

DB_NAME = "manutencao.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS maquinas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            status_funcionamento TEXT NOT NULL,
            usa_preditiva INTEGER DEFAULT 0
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS manutencao_preventiva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maquina_id INTEGER,
            FOREIGN KEY (maquina_id) REFERENCES maquinas(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS manutencao_corretiva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maquina_id INTEGER,
            FOREIGN KEY (maquina_id) REFERENCES maquinas(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS manutencao_preditiva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maquina_id INTEGER,
            status_cor TEXT NOT NULL,
            FOREIGN KEY (maquina_id) REFERENCES maquinas(id)
        );
        """)

        conn.commit()
