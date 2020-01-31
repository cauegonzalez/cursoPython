# coding=UTF-8
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep

# jogadores = {}
# jogador = {}
# for i in range (1, 5):
#     jogador['nome'] = str(input('Nome: '))
#     jogador['valor'] = randint(1, 6)
#     jogadores['jogador'+str(i)] = jogador.copy()
# print(jogadores)

# nomeVencedor = ''
# maiorValor = i = 0
# for key, value in jogadores.items():
#     if i == 0 or maiorValor < value['valor']:
#         maiorValor = value['valor']
#         nomeVencedor = value['nome']
# print(f'vencedor: {nomeVencedor} tirou {maiorValor}')
jogadores = {}
print('Valores sorteados: ')
for i in range(1, 5):
    jogadores['jogador'+str(i)] = randint(1, 6)

for key, value in jogadores.items():
    print(f'\tO {key} tirou {value}')
    sleep(1)
print('Ranking dos jogadores:')
i = 1
for jogador in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'\t{i}º lugar: {jogador} com {jogadores[jogador]}')
    i += 1
    sleep(1)
    