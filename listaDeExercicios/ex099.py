# coding=UTF-8
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep

def maior(* valores):
    tamanho = len(valores)
    maior = 0
    print('Analisando os valores passados...')
    if tamanho > 0:
        maior = max(valores)
        for i in valores:
            print(f'{i} ', end='', flush=True)
            sleep(0.3)
    print(f'| Foram informados {tamanho} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


def linha():
    print('-' * 30)


maior(2, 4, 8, 9)
linha()
maior(2, 5, 7, 40, -8, -9)
linha()
maior(6)
linha()
maior()