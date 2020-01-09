# coding=UTF-8
# Crie um programa que leia um valor inteiro qualquer e mostre na tela sua tabuada, utilizando um laço for
valor = int(input('Digite um número inteiro: '))

for i in range(0, 11):
    print('{} x {}  = {}'.format(valor, i, valor * i))
