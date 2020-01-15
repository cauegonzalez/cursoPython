# coding=UTF-8
# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# - Quantas pessoas foram cadastradas
# - Uma listagem com as pessoas mais pesadas
# - Uma listagem com as pessoas mais leves

pessoas = list()
pessoa = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

maiorPeso = menorPeso = 0
maisLeves = list()
maisPesadas = list()
for key, p in enumerate(pessoas):
    if key == 0 or p[1] < menorPeso:
        menorPeso = p[1]
    if key == 0 or p[1] > maiorPeso:
        maiorPeso = p[1]

for p in pessoas:
    if p[1] == menorPeso:
        maisLeves.append(p[0])
    elif p[1] == maiorPeso:
        maisPesadas.append(p[0])

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorPeso:.1f} Kg. Peso de {maisPesadas}')
print(f'O menor peso foi de {menorPeso:.1f} Kg. Peso de {maisLeves}')