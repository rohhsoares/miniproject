import os
import sqlite3


CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), 'farmacia.db')

def conectar():
    conn = sqlite3.connect(CAMINHO_BANCO)
    return conn


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    categoria TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()