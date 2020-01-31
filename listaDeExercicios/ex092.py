# coding=UTF-8
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (considerar 35 anos).
from datetime import date

anoAtual = date.today().year

pessoa = {}
pessoa['nome'] = str(input('Nome: ')).strip()
anoNascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = anoAtual - anoNascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - anoNascimento) + 35
# print(pessoa)
for key, value in pessoa.items():
    print(f'    - {key.capitalize()} tem o valor: {value}')