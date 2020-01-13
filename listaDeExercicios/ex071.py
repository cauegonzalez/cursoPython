# coding=UTF-8
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs.: Considere que o casixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

nomeBanco = 'BANCO CFG'
print('==' * 22)
print(f'{nomeBanco:^44}')
print('==' * 22)
valorSaque = int(input('Qual valor você deseja sacar? R$ '))

# MINHA SOLUCAO
# quantidadeCinquenta = quantidadeVinte = quantidadeDez = quantidadeUm = resto = 0

# if valorSaque > 50:
#     quantidadeCinquenta = int(valorSaque/50)
#     valorSaque -= quantidadeCinquenta * 50
#     print(f'Total de {quantidadeCinquenta} cédulas de R$ 50')
# if valorSaque > 20:
#     quantidadeVinte = int(valorSaque/20)
#     valorSaque -= quantidadeVinte * 20
#     print(f'Total de {quantidadeVinte} cédulas de R$ 20')
# if valorSaque > 10:
#     quantidadeDez = int(valorSaque/10)
#     valorSaque -= quantidadeDez * 10
#     print(f'Total de {quantidadeDez} cédulas de R$ 10')
# if valorSaque >= 1:
#     quantidadeUm = int(valorSaque/1)
#     valorSaque -= quantidadeUm * 1
#     print(f'Total de {quantidadeUm} cédulas de R$ 1')

# SOLUÇÃO DO GUANABARA
valorCedula = 50
totalCedulas = 0

while True:
    if valorSaque >= valorCedula:
        valorSaque -= valorCedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R$ {valorCedula}')

        if valorCedula == 50:
            valorCedula = 20
        elif valorCedula == 20:
            valorCedula = 10
        elif valorCedula == 10:
            valorCedula = 1
        
        totalCedulas = 0
        if valorSaque == 0:
            break

print('==' * 22)
print(f'Volte sempre ao Banco CFG! Tenha um bom dia!')
