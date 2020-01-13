# coding=UTF-8
# Faça um programa que leia um número inteiro e mostre seu fatorial:

# SOLUÇÃO DO GUANABARA
# from math import factorial
# numero = int(input('Digite um número: '))
# fatorial = factorial(numero)
# print('O resultado de {}! é {}'.format(numero, fatorial))

minha solução
numero = int(input('Digite um número: '))
n = numero
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
print('O resultado de {}! é {}'.format(numero, fatorial))
