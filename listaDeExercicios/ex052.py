# coding=UTF-8
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input('Digite um número inteiro: '))
primo = True
# for i in range(2, numero):
#     if numero % i == 0:
#         primo = False
#         break
# if primo:
#     print('{} é um número primo'.format(numero))
# else:
#     print('{} NÃO é um número primo'.format(numero))

total = 2
print('\033[33m1', end=' ')
for i in range(2, numero):
    if numero % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')

print('\033[33m{}'.format(numero), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
