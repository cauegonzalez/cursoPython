# coding=UTF-8
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.

termos = int(input('Digite a quantidade de termos deseja visualizar: '))
i = 3
termo1 = 0
termo2 = 1
if termos >= 1:
    print(termo1, end=' ')
if termos >= 2:
    print(termo2, end=' ')

while i < termos + 1:
    termoAtual = termo1 + termo2
    print('{} '.format(termoAtual), end='')
    termo1 = termo2 
    termo2 = termoAtual
    i += 1
print('\nACABOU')
