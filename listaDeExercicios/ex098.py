# coding=UTF-8
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
    linha()
    passo = abs(passo)
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    if inicio > fim:
        fim = fim -1
        passo *= -1
    else:
        fim = fim + 1

    for i in range(inicio, fim, passo):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')
    linha()


def linha():
    print('-' * 30)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
linha()

contador(inicio, fim, passo)