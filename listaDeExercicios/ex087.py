# coding=UTF-8
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta e:
# - A soma de todos os valores pares digitados
# - A soma dos valores da terceira coluna
# - O maior valor da segunda linha

linhas = list()
colunas = list()
for i in range(0,3):
    for j in range(0,3):
        aux = int(input(f'Digite o valor da posição [{i}, {j}]: '))
        colunas.append(aux)
    linhas.append(colunas[:])
    colunas.clear()

print('--' * 19)
somaPares = 0
somaTerceiraColuna = 0
maiorSegundaLinha = 0
for i in range(0, 3):
    for j in range(0, 3):
        if linhas[i][j] % 2 == 0:
            somaPares += linhas[i][j]
        if j == 2:
            somaTerceiraColuna += linhas[i][j]
        if i == 1:
            if j == 0 or maiorSegundaLinha < linhas[i][j]:
                maiorSegundaLinha = linhas[i][j]
        print(f'[ {linhas[i][j]:^5} ]', end='')
    print()
print('--' * 19)
print(f'A soma dos valores pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é: {maiorSegundaLinha}')