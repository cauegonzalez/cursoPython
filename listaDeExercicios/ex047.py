# coding=UTF-8
# Faça um programa que mostre na tela todos os números pares que etão no intervalo entre 1 e 50

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i, end=' ')
# print('ACABOU')

# outra forma de resolver, utilizando passo 2
for i in range(2, 51, 2):
    print(i, end=' ')
print('ACABOU')