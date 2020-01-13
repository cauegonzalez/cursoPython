# coding=UTF-8
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

soma = i = 0
while True:
    numero = int(input('Digite um número inteiro qualquer ou 999 para parar: '))
    if numero == 999:
        break
    soma += numero
    i += 1
print(f'A soma dos {i} números digitados é {soma}')
