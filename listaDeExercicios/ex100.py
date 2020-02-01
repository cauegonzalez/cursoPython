# coding=UTF-8
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e 
# a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia():
    lista = []
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numero = randint(0, 99)
        lista.append(numero)
        print(f'{numero} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
    return lista


def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


def linha():
    print('-' * 30)


lista = sorteia()
soma_par(lista)