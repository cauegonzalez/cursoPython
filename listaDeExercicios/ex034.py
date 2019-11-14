# coding=UTF-8
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print('O aumento do salário é de R$ {:.2f} e seu valor é R$ {:.2f}'.format(aumento, salario+aumento))