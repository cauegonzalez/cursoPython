# Crie um programa que leia o salário de uma pessoa e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o salário atual: '))

novoSalario = salario + (salario * (15 / 100))
print('O seu salário era R$ {:.2f} e irá par R$ {:.2f}.'.format(salario, novoSalario))
