import sqlite3
from datetime import datetime

DB_NAME = "database/movimentos.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configuracao (
            id INTEGER PRIMARY KEY,
            monitoramento TEXT NOT NULL,
            ativacao_em TEXT
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO configuracao
        (id, monitoramento, ativacao_em)
        VALUES (1, 'DESATIVADO', NULL)
    """)

    conexao.commit()
    conexao.close()


def registrar_movimento():
    conexao = conectar()
    cursor = conexao.cursor()

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO movimentos (data_hora) VALUES (?)",
        (data_hora,)
    )

    conexao.commit()
    conexao.close()

    print(f"Movimento registrado: {data_hora}")


def obter_status():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT monitoramento, ativacao_em
        FROM configuracao
        WHERE id = 1
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado
def definir_status(status, ativacao_em=None):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE configuracao
        SET monitoramento = ?, ativacao_em = ?
        WHERE id = 1
    """, (status, ativacao_em))

    conexao.commit()
    conexao.close()


def obter_status_monitoramento():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT monitoramento
        FROM configuracao
        WHERE id = 1
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado[0]
def contar_movimentos_hoje():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM movimentos
        WHERE date(data_hora) = date('now', 'localtime')
    """)

    resultado = cursor.fetchone()[0]

    conexao.close()

    return resultado


def obter_ultimo_movimento():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT data_hora
        FROM movimentos
        ORDER BY id DESC
        LIMIT 1
    """)

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        return resultado[0]

    return None
def obter_ultimos_movimentos(limite=10):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT data_hora
        FROM movimentos
        ORDER BY id DESC
        LIMIT ?
    """, (limite,))

    resultados = cursor.fetchall()

    conexao.close()

    return [resultado[0] for resultado in resultados]
