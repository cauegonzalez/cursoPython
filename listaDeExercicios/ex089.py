# coding=UTF-8
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
aluno = list()
notas = list()
i = 0
while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    media = (notas[0] + notas[1]) / 2
    aluno.append(media)
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    i += 1
print('-' * 50)
print('{:<5}{:<35}{:>10}'.format('Nº', 'Nome', 'Média'))
print('-' * 50)
for numero, aluno in enumerate(alunos):
    print('{:<5}{:<35}{:>10.1f}'.format(numero, aluno[0], aluno[2]))
print('-' * 50)

while True:
    numeroAluno = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if numeroAluno == 999:
        print('Saindo do programa')
        break
    if numeroAluno < 0 or numeroAluno > len(alunos) - 1:
        print('Índice inválido! ', end='')
        continue
    print(f'Notas de {alunos[numeroAluno][0]} são: {alunos[numeroAluno][1]}')
print('-' * 50)
