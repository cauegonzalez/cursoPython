# coding=UTF-8
# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))

maior = menor = 0
for key, n in enumerate(numeros):
    if key == 0 or n < menor:
        menor = n
    if key == 0 or n > maior:
        maior = n

print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi: {maior} ou {max(numeros)}')
print(f'O menor valor sorteado foi: {menor} ou {min(numeros)}')