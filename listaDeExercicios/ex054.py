# coding=UTF-8
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são 
# maiores. Considerar maioridade com 21 anos
from datetime import date 

anoAtual = date.today().year
maiores = 0
menores = 0
for i in range(0, 7):
    anoNascimento = int(input('Digite o ano de nascimento da pessoa nº {}: '.format(i + 1)))

    idade = anoAtual - anoNascimento 
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print('Da listagem informada, {} pessoas são maiores de idade e {} são menores'.format(maiores, menores))
