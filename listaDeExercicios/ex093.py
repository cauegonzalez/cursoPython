# coding=UTF-8
# Crie um programa que gerencue o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['nome'] = str(input('Nome do jogador: ')).strip()
qtdePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
golsPorPartida = list()
for i in range(0, qtdePartidas):
    golsPorPartida.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i + 1}? ')))
    
jogador['listaGols'] = golsPorPartida[:]
jogador['totalGols'] = sum(golsPorPartida)
print('-=' * 33)
print(jogador)
print('-=' * 33)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')
print('-=' * 33)

print(f'O jogador {jogador["nome"]} jogou {qtdePartidas} partidas.')
for i in range(0, qtdePartidas):
    print(f'\t=> Na partida {i + 1}, fez {golsPorPartida[i]} gols.')
print(f'Foi um total de {jogador["totalGols"]} gols.')
