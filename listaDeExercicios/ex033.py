# coding=UTF-8
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))

if numero1 >= numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

if numero3 >= maior:
    maior = numero3

if numero3 <= menor:
    menor = numero3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))