# coding=UTF-8
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve pergutnar ao usuário se ele quer ou não continuar a digitar valores

numero = soma = i = menor = maior = 0
continuar = 'S'
while continuar != 'N':
    numero = int(input('Digite um número inteiro qualquer: '))
    soma += numero
    i += 1
    if i == 1:
        menor = maior = numero 

    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

    continuar = input('Deseja continuar a digitar números? [S/N] ').strip().upper()[0]
media = soma / i
print('\nA média dos {} números digitados é {}'.format(i, media))
print('O menor número é {} e o maior número é {}'.format(menor, maior))
