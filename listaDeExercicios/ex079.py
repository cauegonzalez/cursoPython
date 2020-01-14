# coding=UTF-8
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lita. Caso o número já exista lá dentro, 
# ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = list()
while True:
    aux = int(input('Digite um valor inteiro: '))
    if aux not in valores:
        valores.append(aux)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não será adicionado!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print('Você digitou a lista: {}'.format(valores))
