# coding=UTF-8
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date 

ano = int(input('Digite o ano do nascimento do atleta: '))

idade = date.today().year - ano

if idade <= 9:
    print('Categoria \033[36mMIRIM\033[m, idade: {}'.format(idade))
elif idade > 9 and idade <= 14:
    print('Categoria \033[36mINFANTIL\033[m, idade: {}'.format(idade))
elif idade > 14 and idade <= 19:
    print('Categoria \033[36mJUNIOR\033[m, idade: {}'.format(idade))
elif idade > 19 and idade <= 25:
    print('Categoria \033[36mSÊNIOR\033[m, idade: {}'.format(idade))
else:
    print('Categoria \033[36mMASTER\033[m, idade: {}'.format(idade))