# coding=UTF-8
# Crie um programa que tenha uma função chamada leia_int(), que vai funcionar de forma semelhante à função input() do python, 
# só que fazendo a validação para aceitar apenas um valor numérico.

def leia_int(msg):
    """
    -> Espera receber um valor inteiro pelo teclado informando a mensagem recebida por parâmetro
    :param msg: mensagem
    :return: o inteiro informado
    """
    n = str(input(msg))
    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um número inteiro válido\033[m') 
        n = str(input(msg))

    return n


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')