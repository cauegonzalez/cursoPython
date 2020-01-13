# coding=UTF-8
# Desenvolva um programa leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# - Quantas vezes apareceu o valor 9
# - Em que posição foi digitado o primeiro valor 3
# - Quais foram os números pares

maior = menor = 0
# valor1 = int(input('Digite o valor 1: '))
# valor2 = int(input('Digite o valor 2: '))
# valor3 = int(input('Digite o valor 3: '))
# valor4 = int(input('Digite o valor 4: '))

# numeros = (valor1, valor2, valor3, valor4)
numeros = (int(input('Digite o valor 1: ')),
           int(input('Digite o valor 2: ')),
           int(input('Digite o valor 3: ')),
           int(input('Digite o valor 4: ')))

print(f'Você digitou os valores {numeros}')
print(f'O valor nove apareceu: {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

print('Os números pares foram: ', end='')
for key, value in enumerate(numeros):
    if value % 2 == 0:
        print(f'{value}', end=' ')

print('\nFIM do PROGRAMA')
