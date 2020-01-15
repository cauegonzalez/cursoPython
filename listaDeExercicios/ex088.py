# coding=UTF-8
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

todosOsJogos = list()
jogo = list()
print('--' * 15)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('--' * 15)
qtdeJogos = int(input(f'Quantos jogos você deseja? '))
for i in range(0, qtdeJogos):
    for j in range(0, 6):
        aux = randint(1, 60)
        while aux in jogo:
            aux = randint(1, 60)
        jogo.append(aux)
    jogo.sort()
    todosOsJogos.append(jogo[:])
    jogo.clear()
    
print('--' * 15)
print('{:^30}'.format('SORTEANDO OS JOGOS'))
print('--' * 15)
for i in range(0, qtdeJogos):
    sleep(1)
    print(f'Jogo {i + 1}: {todosOsJogos[i]}')
print('--' * 15)