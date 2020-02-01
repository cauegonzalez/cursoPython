# coding=UTF-8
def cabecalho(msg, tamanho):
    mostra_linha(tamanho)
    print(f'{msg:^{tamanho}}')
    mostra_linha(tamanho)


def mostra_linha(tamanho):
    print('-' * tamanho)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'A soma A + B = {s}')


# Asterisco no parâmetro é desempacotamento. quantidade de parâmetros fica variável pois o python transforma em tupla
def soma_varios(* valores):
    s = 0
    for numero in valores:
        s += numero
    print(f'Somando os valores {valores} temos {s}')


# Trabalhando com Funções
print('====Exercício Aula 20====')

cabecalho('Minhas primeiras funções em Python', 40)
soma(b=4, a=5)
soma(7, 9)
soma_varios(2, 4, 8, 13)
soma_varios(24, 81, 32, 9, 0, 15, 29)