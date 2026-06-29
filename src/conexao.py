import mysql.connector
from mysql.connector import Error


def criar_conexao():
    """
    Estabelece a conexão com o banco de dados MySQL local.
    Retorna o objeto de conexão se for bem-sucedido ou None se falhar.
    """
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',  # Usuário padrão do MySQL local
            password='SUA SENHA AQUI',  # Coloque a senha do seu MySQL local aqui (se houver)
            database='pinterest_db'  # Nome do banco que o seu DBA (Integrante B) vai definir
        )

        if conexao.is_connected():
            print("=> Conexão com o MySQL estabelecida com sucesso!")
            return conexao

    except Error as erro:
        print(f"X Erro ao tentar conectar ao banco de dados: {erro}")
        return None


def fechar_conexao(conexao):
    """
    Encerra a conexão com o banco de dados de forma segura.
    """
    if conexao and conexao.is_connected():
        conexao.close()
        print("=> Conexão com o banco de dados encerrada com segurança.")
