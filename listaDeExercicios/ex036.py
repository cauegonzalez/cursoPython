# coding=UTF-8
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
prazo = int(input('Em quantos anos deseja parcelar o empréstimo? '))

prazoTotal = prazo * 12

prestacao = valor / prazoTotal

limitePrestacao = salario * 0.3

print('O valor a ser pago é de {} parcelas de R$ {:.2f}.'.format(prazoTotal, prestacao))
if prestacao > limitePrestacao:
    print('\033[31mO empréstimo não foi aprovado, pois o valor da prestação excede o limite de R$ {:.2f}'.format(limitePrestacao))
else:
    print('\033[32mO empréstimo foi aprovado!')
    