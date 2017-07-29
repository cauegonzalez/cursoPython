# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
aluno1 = 'Cauê'
aluno2 = 'Malu'
aluno3 = 'Raiani'
aluno4 = 'Aline'

listAlunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(listAlunos)

print('O aluno sorteado foi o {}.'.format(sorteado))
