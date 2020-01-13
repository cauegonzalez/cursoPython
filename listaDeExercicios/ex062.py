# coding=UTF-8
# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i = 0
totalTermos = termos = 10
while termos > 0:
    while i < termos:
        print('{} '.format(primeiroTermo), end='')
        primeiroTermo += razao
        i += 1
    i = 0
    termos = int(input('PAUSA\nVocê deseja visualizar mais quantos termos? '))
    totalTermos += termos
print('O programa finalizou mostrando {} termos no total '.format(totalTermos))
