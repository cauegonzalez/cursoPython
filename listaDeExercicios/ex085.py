# coding=UTF-8
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# numeros = list()
# numeros.append(list())
# numeros.append(list())
numeros = [[], []]
for i in range(1,8):
    aux = int(input(f'Digite o {i}º valor: '))
    numeros[aux % 2].append(aux)

print('--' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')