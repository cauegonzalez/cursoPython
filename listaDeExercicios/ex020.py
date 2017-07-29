# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample
aluno1 = 'Aline Gonzalez'
aluno2 = 'Cauê Gonzalez'
aluno3 = 'Malu Gonzalez'
aluno4 = 'Raiani Gonzalez'

listAlunos = [aluno1, aluno2, aluno3, aluno4]
tamanho = len(listAlunos)
ordem = sample(listAlunos, tamanho)

# print('A ordem de apresentação é {}, {}, {}, {}.'.format(ordem[0], ordem[1], ordem[2], ordem[3]))
print('A ordem de apresentação é {}.'.format(ordem))
