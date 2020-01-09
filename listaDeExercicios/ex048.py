# coding=UTF-8
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três que etão no intervalo entre 1 e 500
soma = 0
contador = 0
# for i in range(1, 501):
#     if i % 2 == 1 and i % 3 == 0:
#         soma += i
#         contador += 1

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        contador += 1

print('A soma dos {} valores é {}'.format(contador, soma))
