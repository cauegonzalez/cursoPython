# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#   Ex.:
#   - Digite um número: 1834
#   - unidade: 4
#   - dezena: 3
#   - centena: 8
#   - milhar: 1
#
import math

#   Abordagem com tratamento de string
numero = input('Digite um número entre 0 e 9999: ')


print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))

#
#   Abordagem com tratamento matemático
#
print('------outra abordagem------')
numero = int(numero)

unidade = numero % 10
numero = math.trunc(numero / 10)
dezena = numero % 10
numero = math.trunc(numero / 10)
centena = numero % 10
numero = math.trunc(numero / 10)
milhar = numero % 10

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))