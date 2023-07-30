import mysql.connector
from sql_functions import funcoes

configuracao = {
    'user':'root',
    'password':'Bl@cK200',
    'host':'127.0.0.1',
    'database':'estudo_CC'}

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
    funcoes.consultar(table)


