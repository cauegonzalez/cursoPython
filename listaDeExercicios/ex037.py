# coding=UTF-8
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input('Digite o número a ser convertido: '))
print("""Escolha a base de conversão considerando: 
    - [ 1 ] converter para BINÁRIO 
    - [ 2 ] converter para OCTAL 
    - [ 3 ] converter para HEXADECIMAL""")
base = int(input('Sua escolha: '))

if base == 1:
    # numeroConvertido = "{0:b}".format(numero)
    numeroConvertido = bin(numero)
    nomeBase = 'binário'
elif base == 2:
    # numeroConvertido = "0o{0:o}".format(numero)
    numeroConvertido = oct(numero)
    nomeBase = 'octal'
elif base == 3:
    # numeroConvertido = "0x{0:x}".format(numero)
    numeroConvertido = hex(numero)
    nomeBase = 'hexadecimal'
else:
    print('Operação não permitida')
    exit()
print('O número {} em {} é \033[32m{}'.format(numero, nomeBase, numeroConvertido))
