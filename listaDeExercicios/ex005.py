# Crie um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor.
num = int(input('Digite um número inteiro: '))
prev = num - 1
next = num + 1
print('Analisando o número {}, seu antecessor é {} e seu sucessor é {}'.format(num, prev, next))
