# coding=UTF-8
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar ao serviço militar
# Se já passou o tempo do alistamento
# Seu programa também deverá mostrar o tempo que faltoa ou que passou do prazo

from datetime import date 

ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano

if idade == 18:
    print('Já é hora do seu alistamento ao serviço militar obrigatório')
elif idade < 18:
    print('Você deverá se alistar em {} anos'.format(18 - idade))
else:
    print('Seu prazo para o alistamento ao serviço militar obrigatório já excedeu em {} anos'.format(idade - 18))
    