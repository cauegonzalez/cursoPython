# coding=UTF-8
# Faça um programa que tenha uma função chamada notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# 
# Adicione também as docstrings da função

def notas(* notas, situacao=False):
    """
    -> Espera receber diversas notas e armazena o resumo em um dicionário
    :param notas: as notas de cada aluno
    :param situacao: (opcional) se verdadeiro, armazena a situação de acordo com a média da turma
    :return: o dicionário com o resumo das notas informadas
    """
    turma = {}
    turma['total'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['media'] = sum(notas)/turma['total']
    if situacao:
        if turma['media'] >= 7:
            turma['situacao'] = 'Boa'
        elif 5 <= turma['media'] < 7:
            turma['situacao'] = 'Razoável'
        else:
            turma['situacao'] = 'Ruim'

    return turma


turma = notas(9, 7, 6, 7, 7, situacao=True)
print(turma)
