# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçẽos possíveis sobre ele.
print('====Exercício Aula 06====')
valor1  = input('Digite algo: ')
print('{} possui o tipo primitivo {}'.format(valor1, type(valor1)))
if valor1.isnumeric():
    print('{} é numérico'.format(valor1))
else:
    print('{} não é numérico'.format(valor1))
if valor1.isalpha():
    print('{} é alfabético'.format(valor1))
else:
    print('{} não é alfabético'.format(valor1))
if valor1.isalnum():
    print('{} é alfanumérico'.format(valor1))
else:
    print('{} não é alfanumérico'.format(valor1))
if valor1.isupper():
    print('{} está somente em maiúsculas'.format(valor1))
else:
    print('{} não está somente em maiúsculas'.format(valor1))
if valor1.islower():
    print('{} está somente em minúsculas'.format(valor1))
else:
    print('{} não está somente em minúsculas'.format(valor1))
if valor1.isprintable():
    print('{} é do tipo printable'.format(valor1))
else:
    print('{} não é do tipo printable'.format(valor1))
if valor1.isspace():
    print('{} contém somente espaços'.format(valor1))
else:
    print('{} não contém somente espaços'.format(valor1))
if valor1.istitle():
    print('{} está capitalizado'.format(valor1))
else:
    print('{} não está capitalizado'.format(valor1))
