# coding=UTF-8
# Crie um programa que receba uma sequencia de números inteiros e informe sua soma. A condição de parada é quando o número 999 for digitado
print('====Exercício Aula 15====')
soma = 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    soma += numero
# print('A soma dos valores digitados é {}'.format(soma))
print(f'A soma dos valores digitados é {soma}')