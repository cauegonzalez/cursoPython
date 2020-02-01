# coding=UTF-8
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(mensagem):
    tamanho = len(mensagem) + 10
    print('~' * tamanho)
    print(f'{mensagem:^{tamanho}}')
    print('~' * tamanho)


# programa principal
mensagem = str(input('Escreva a mensagem que quer ver formatada: '))
escreva(mensagem)