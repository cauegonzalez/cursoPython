# coding=UTF-8
# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

jogador = int(input('Pensei em um número de 0 a 5, duvido que você acerte: '))
computador = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você acertou, parabéns!')
else:
    print('Você errou, pensei no número {}'.format(computador))