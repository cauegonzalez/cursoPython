# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçẽos possíveis sobre ele.
var = input('Digite algo: ')
print('O tipo primitivo de {} é: {}'.format(var, type(var)))
print('{} só tem espaços? {}'.format(var, var.isspace()))
print('{} é alfabético? {}'.format(var, var.isalpha()))
print('{} é alfanumérico? {}'.format(var, var.isalnum()))
print('{} está em maiúsculas? {}'.format(var, var.isupper()))
print('{} está em minúsculas? {}'.format(var, var.islower()))
print('{} está capitalizada? {}'.format(var, var.istitle()))
