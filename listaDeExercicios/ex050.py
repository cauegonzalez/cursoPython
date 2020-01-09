# coding=UTF-8
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0
contador = 0
for i in range(1, 7):
    valor = int(input('Digite o {}º número inteiro: '.format(i)))
    if valor % 2 == 0:
        soma += valor
        contador += 1

print('A soma dos {} números pares digitados é: {}'.format(contador, soma))
