# coding=UTF-8
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

# termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# print('{} '.format(termo))
# for i in range(1, 11):
#     termo += razao
#     print('{} '.format(termo))

# outra forma de resolver:

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

decimoTermo = primeiroTermo + (10 - 1) * razao
for i in range(primeiroTermo, decimoTermo + 1, razao):
    primeiroTermo += razao
    print('{} -> '.format(primeiroTermo), end='')
print('ACABOU')
