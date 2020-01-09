# coding=UTF-8
# Crie um programa que receba uma quantidade de números e informe o somatório ao final
print('====Exercício Aula 13====')
somatorio = 0
total = int(input('Digite a quantidade de itens a serem somados: '))

for i in range(0, total):
    n = int(input('Digite um número inteiro: '))
    somatorio += n 

print('O somatório dos números digitados é: {}!'.format(somatorio))