# coding=UTF-8
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# - Quantas pessoas foram cadastradas
# - A média de idade do grupo
# - Uma lista com todas as mulheres
# - Uma lista com todas as pessoas com idade acima da média

listaPessoas = []
mulheres = []
maioresMedia = []
pessoa = {}
somaIdade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Valor incorreto. Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    listaPessoas.append(pessoa.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'- A quantidade de pessoas cadastradas foi: {len(listaPessoas)}')
media = somaIdade / len(listaPessoas)
print(f'- A média de idade do grupo foi: {media:.2f}')
print(f'- A lista com as mulheres cadastradas é: {mulheres}')
print(f'- Lista das pessoas que estão acima da média: ')
for pessoa in listaPessoas:
    if pessoa['idade'] >= media:
        print('\t', end='')
        for key, value in pessoa.items():
            print(f'{key.capitalize()} = {value}; ', end='')
        print()
print()
print('PROGRAMA ENCERRADO')
