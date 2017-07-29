# Crie um programa que rreceba um valor e calcule sua raiz quadrada
# import math
# print('====Exercício Aula 08====')
# valor1  = int(input('Digite um valor: '))
# raiz = math.sqrt(valor1)
# print('A raiz quadrada de {0} é: {1}'.format(valor1, raiz))

# Outra forma de fazer a mesma coisa
# (assim, ao invés de importar a biblioteca toda, importa somente as funcionalidades que pretendo utilizar, economizando memória):
from math import sqrt, floor
print('====Exercício Aula 08====')
valor1  = int(input('Digite um valor: '))
raiz = sqrt(valor1)
print('A raiz quadrada de {0} é: {1}'.format(valor1, floor(raiz)))