# coding=UTF-8
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

for i in range(1, 6):
    peso = float(input('Digite o peso da pessoa nº {}: '.format(i)))

    if i == 1:
        maior = menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 

print('Da listagem informada, {} Kg é o maior peso e {} Kg é o menor'.format(maior, menor))
