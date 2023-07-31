from sql_functions import funcoes
from time import sleep

table = input('Escolha a tabela: ')
welcomeMessage = 'Welcome to MySQL Connector!'
welcomeMessage.center(20)
print('-'*40)
print(' '*6 + welcomeMessage)
print('-'*40)
while True:
    sleep(2)
    print('1 - Consult data')
    print('2 - Insert data')
    print('3 - Quit')
    print('-' * 40)
    opc = int(input('Select an option: '))
    print('-' * 40)

    if opc == 1:
        funcoes.consultar(table)
    elif opc == 2:
        funcoes.inserir(table)
    elif opc == 3:
        print('Exiting the system...')
        sleep(2)
        print('See you soon!')
        break
    else:
        print('Invalid option. Please try again...')


