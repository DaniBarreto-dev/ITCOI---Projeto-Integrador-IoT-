import sqlite3
from pathlib import Path
from datetime import datetime

# Caminho absoluto para criar/acessar o arquivo do banco de dados na pasta backend
CAMINHO_BANCO = Path(__file__).parent / "banco.db"

def conectar():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row  # Retorna resultados acessíveis por chave/nome de coluna
    return conexao

def criar_tabela():
    """Cria a tabela 'medicoes' se ela ainda não existir."""
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS medicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distancia REAL NOT NULL,
            data_hora TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def salvar_medicao(distancia: float):
    """Salva uma nova leitura de distância com a data e hora atuais."""
    conexao = conectar()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conexao.execute(
        "INSERT INTO medicoes (distancia, data_hora) VALUES (?, ?)",
        (distancia, data_hora)
    )
    conexao.commit()
    conexao.close()

def listar_medicoes(limite: int = 50):
    """Retorna as últimas medições salvas no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, distancia, data_hora FROM medicoes ORDER BY id DESC LIMIT ?",
        (limite,)
    )
    linhas = cursor.fetchall()
    conexao.close()
    
    # Converte cada linha do SQLite em um dicionário Python
    return [dict(linha) for linha in linhas]