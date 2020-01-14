# coding=UTF-8
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lita.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# No final, mostre o conteúdo das 3 listas geradas

valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor inteiro: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Você digitou a lista: {valores}')
print(f'Os números pares estão na lista: {pares}')
print(f'Os números ímpares estão na lista: {impares}')