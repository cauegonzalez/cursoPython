# coding=UTF-8
def cabecalho(msg, tamanho):
    """
    Cria um cabeçalho, utilizando linhas tracejadas para envolver o texto informado
    :param msg: mensagem a ser escrita no cabeçalho
    :param tamanho: tamanho da linha a ser utilizada como divisor
    :return: sem retorno
    """
    mostra_linha(tamanho)
    print(f'{msg:^{tamanho}}')
    mostra_linha(tamanho)


def mostra_linha(tamanho):
    """
    Cria uma linha com tamanho personalisado
    :param tamanho: tamanho da linha a ser criada
    :return: sem retorno
    """
    print('-' * tamanho)


def soma(a, b):
    """
    Soma dois valores
    :param a: primeiro termo da adição
    :param b: segundo termo da adição
    :return: sem retorno
    """
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'A soma A + B = {s}')


# Asterisco no parâmetro é desempacotamento. quantidade de parâmetros fica variável pois o python transforma em tupla
def soma_varios(* valores):
    """
    Soma diversos valores
    :param valores: lista de valores a serem somados
    """
    s = 0
    for numero in valores:
        s += numero
    print(f'Somando os valores {valores} temos {s}')


# Trabalhando com Funções (parte 2)
print('====Exercício Aula 21====')

help(cabecalho)
help(mostra_linha)
help(soma)
help(soma_varios)
exit()
cabecalho('Minhas primeiras funções em Python', 40)
soma(b=4, a=5)
soma(7, 9)
soma_varios(2, 4, 8, 13)
soma_varios(24, 81, 32, 9, 0, 15, 29)