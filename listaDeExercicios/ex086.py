# coding=UTF-8
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

linhas = list()
colunas = list()
for i in range(0,3):
    for j in range(0,3):
        aux = int(input(f'Digite o valor da posição [{i}, {j}]: '))
        colunas.append(aux)
    linhas.append(colunas[:])
    colunas.clear()

print('--' * 20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {linhas[i][j]:^5} ]', end='')
    print()
