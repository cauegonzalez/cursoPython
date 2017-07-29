"""
Crie um programa que imprima um número randômico entre 0 e 1 e outro número randômico entre 1 e 10
"""
import random
print('====Exercício Aula 08====')
valor1  = random.random()
valor2  = random.randint(1, 10)
print('O número randômico entre 0 e 1 é: {}'.format(valor1))
print('O número randômico entre 1 e 10 é: {}'.format(valor2))