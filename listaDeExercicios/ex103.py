# coding=UTF-8
# Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>', gols=0):
    """
    -> Informa a ficha do jogador.
    :param nome: (opcional) o nome do jogador sendo analisado.
    :param gols: (opcional) quantidade de gols feitos no campeonato.
    :return: (str) nome do jogador e quantidade de gols
    """
    return 'O jogador '+ nome +' fez '+ str(gols)+' gol(s) no campeonato.'


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
if nome == '' and gols != '':
    print(ficha(gols=gols))
    exit()
if gols == '' and nome != '':
    print(ficha(nome=nome))
    exit()
if nome == '' and gols == '':
    print(ficha())
    exit()
print(ficha(nome, gols))