# coding=UTF-8
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
# aluno['situacao'] = ('Aprovado' if aluno['media'] >= 7 else 'Reprovado')
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5<= aluno['media'] < 7: 
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-' * 50)
for key, value in aluno.items():
    print(f'\t{key.capitalize()} é {value}')
