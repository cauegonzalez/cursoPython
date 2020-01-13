# coding=UTF-8
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo

while True:
    numero = int(input('\nDigite um número para ver sua tabuada: '))
    print('=' * 30)
    if numero < 0:
        break

    i = 0
    while i < 11:
        produto = numero * i
        print(f'{numero} * {i} = {produto}')
        i += 1
        
    print('=' * 30)
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!')