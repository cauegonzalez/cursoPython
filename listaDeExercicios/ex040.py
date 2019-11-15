# coding=UTF-8
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digite a 2ª nota do aluno: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Aluno \033[31mREPROVADO\033[m com média {:.1f}'.format(media))
elif media >= 5 and media < 7:
    print('Aluno em \033[33mRECUPERAÇÃO\033[m com média {:.1f}'.format(media))
else:
    print('Aluno \033[32mAPROVADO\033[m com média {:.1f}'.format(media))
    