import mysql.connector
from mysql_connection import configuracao

def consultar(tabela):
    try:
        conexao = mysql.connector.connect(**configuracao)
        cursor = conexao.cursor()
        consultar_contato = (f"select * from {tabela}")
        cursor.execute(consultar_contato)
        for id, nome, carga, local in cursor:
            print(f'id: {id} || Nome: {nome} || Carga Horária: {carga} || Local:{local}')
    except mysql.connector.Error as erro:
        if erro.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuário ou senha inválidos')
        elif erro.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados não existe')
        else:
            print(erro)
    else:
        cursor.close()
    conexao.close()

def inserir(tabela):
    nome = input('Digite o nome: ')
    carga_horaria = input('Digite a carga horária: ')
    local = input('Digite a instituição de ensino: ')
    try:
        conexao = mysql.connector.connect(**configuracao)
        cursor = conexao.cursor()  # "cursor()" é instanciado como o objeto que executa comandos SQL.
        inserir_contato = (f"insert into {tabela} (nome, carga_horaria, local) "
                           "values (%s, %s, %s)")
        contato = (nome, carga_horaria, local)
        cursor.execute(inserir_contato, contato)  # Cursor executando com método execute(comando, tupla)
        conexao.commit()
    except mysql.connector.Error as erro:
        if erro.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuário ou senha inválidos')
        elif erro.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados não existe')
        else:
            print(erro)
    else:
        cursor.close()
    conexao.close()



