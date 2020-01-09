# coding=UTF-8
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# from math import ceil
# frase = input('Digite uma frase: ')
# fraseModificada = frase.upper().replace(' ', '')

# tamanho = len(fraseModificada)
# metade = int(ceil(tamanho / 2))
# palindromo = True

# for i in range(0, metade + 1):
#     if fraseModificada[i] != fraseModificada[tamanho -1 - i]:
#         palindromo = False
#         break

# if palindromo:
#     print('"{}" é um palíndromo'.format(frase.upper()))
# else:
#     print('"{}" NÃO é um palíndromo'.format(frase.upper()))

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# fatiamento para obter o inverso sem a necessidade do for
inverso = junto[::-1]
# caso queira fazer o inverso com o for, segue o código
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]

print('Você digitou a frase {} e seu inverso é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')