# coding=UTF-8
# Crie um programa que gerencie o aproveitamento de vários jogadores de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.
# Apresentar também um sistema de visualização de detalhes do aproveitamento de cada jogador.

# TODO: AJUSTAR ERRO DAS LINHAS 31 E 32 E TERMINAR O EXERCÍCIO. PAREI NO MINUTO 42:43 DO VÍDEO Curso Python # 19 - Dicionários


jogadores = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    qtdePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    golsPorPartida = list()
    for i in range(0, qtdePartidas):
        golsPorPartida.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i + 1}? ')))
        
    jogador['listaGols'] = golsPorPartida[:]
    jogador['totalGols'] = sum(golsPorPartida)
    jogadores.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 33)
print(f'{"cod":>3} {"nome":<30}{"gols":<20}{"total":<6}')
for i, atleta in enumerate(jogadores):
    listaDeGols = ''.join(str(atleta['listaGols']))
    print('{:>3} {:<30}{:<20}{:<6}'.format(i, atleta['nome'], listaDeGols, atleta['totalGols']))
# exit()
print('--' * 33)

opcao = 0
while opcao != 999:
    opcao = int(input('Mostrar dados de qual jogador? '))
    if opcao == 999:
        break

    while opcao < 0 or opcao >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {opcao}. Tente novamente! ')
        opcao = int(input('Mostrar dados de qual jogador? '))

    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}:')
    for i, gols in enumerate(jogadores[opcao]['listaGols']):
        print(f'\tNo jogo {i + 1} fez {gols} gols.')
    print('-' * 50)
print('<<< Volte Sempre >>>')
