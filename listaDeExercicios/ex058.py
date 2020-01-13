# coding=UTF-8
# Melhore o jogo do desavio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador deve tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

computador = randint(0,10)
jogador = -1
print('Pensei em um número de 0 a 10, duvido que você acerte:')
print('PROCESSANDO...\n')
sleep(2)
n = 0
while jogador != computador:
    jogador = int(input('Seu {}º palpite: '.format(n + 1)))
    n += 1
    if jogador < computador:
        print('Errou, é maior')
    elif computador < jogador:
        print('Errou, é menor')

print('Você acertou o número com {} tentativa(s)!'.format(n))
if n <= 3:
    print('PARABÉNS')
