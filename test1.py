import mysql.connector

configuracao = {
    'user':'root',
    'password':'Bl@cK200',
    'host':'127.0.0.1',
    'database':'estudo_CC'}
def consultar(tabela):
    try:
        conexao = mysql.connector.connect(**configuracao)
        cursor = conexao.cursor()
        consultar_contato = (f"select * from {tabela}")
        cursor.execute(consultar_contato)
        for nome, carga, local in cursor:
            print(f'Nome: {nome} || Carga Horária: {carga} || Local:{local}')
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



def atualizar(tabela):
    id_ = input('Select id to be updated: ')
    nome = input('Digite o nome: ')
    carga_horaria = input('Digite a carga horária: ')
    local = input('Digite a instituição de ensino: ')
    try:
        conexao = mysql.connector.connect(**configuracao)
        cursor = conexao.cursor()
        atualizar_contato = (f"update {tabela} set nome=%s, carga_horaria=%s, local=%s where id={id_}")
        contato = (nome, carga_horaria, local)
        cursor.execute(atualizar_contato, contato)
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

def apagar(tabela):
    id_ = input('Select id to be deleted: ')
    try:
        conexao = mysql.connector.connect(**configuracao)
        cursor = conexao.cursor()
        delete_contato = (f'delete from {tabela} where id={id_}')
        cursor.execute(delete_contato)
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

table = input('Escolha a tabela: ')

welcomeMessage = 'Welcome to MySQL Connector!'
welcomeMessage.center(20)
print('-'*40)
print(' '*6 + welcomeMessage)
print('-'*40)
print('1 - Consult data')
print('2 - Insert data')
print('3 - Update data')
print('4 - Delete data')
print('5 - Quit')
opc = int(input('Select an option: '))

if opc == 1:
    consultar(table)


