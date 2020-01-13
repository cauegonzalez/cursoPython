# coding=UTF-8
# Crie um programa que receba uma quantidade de números e informe a quantidade de números pares digitados e a quantidade de ímpares
print('====Exercício Aula 14====')
numero = 1
pares = impares = 0

while numero != 0:
    numero = int(input('Digite um número inteiro: '))
    if numero != 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1 

print('Você digitou {} números pares e {} números ímpares'.format(pares, impares))