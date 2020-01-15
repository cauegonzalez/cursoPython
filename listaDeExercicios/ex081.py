# coding=UTF-8
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lita.
# No final, mostre:
# - Quantos números foram digitados
# - A lista de valores, ordenada de forma decrescente
# - Se o valor 5 foi digitado e está ou não na lista

valores = list()
while True:
    valores.append(int(input('Digite um valor inteiro: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você digitou a lista: {valores}')
print(f'A lista digitada tem : {len(valores)}')
valores.sort(reverse=True)
print(f'A lista digitada em ordem decrescente é : {valores}')
if 5 in valores:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 NÃO foi digitado e, portanto, NÃO está na lista')
