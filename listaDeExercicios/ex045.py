# coding=UTF-8
# Crie um programa que faça o computador jogar jokempô com você
from random import randint

escolhaJogador = int(input("""Escolha uma forma para jogar:
    - [ 1 ]: PEDRA
    - [ 2 ]: PAPEL
    - [ 3 ]: TESOURA
"""))
escolhaComputador = randint(1,3)
escolhasPossiveis = {
    1: 'PEDRA',
    2: 'PAPEL',
    3: 'TESOURA',
}

if escolhaJogador == 1:
    if escolhaComputador == 3:
        msg = '\033[32mVocê ganhou pois PEDRA amassa a TESOURA\033[m'
    elif escolhaComputador == 1:
        msg = '\033[33mEMPATE\033[m'
    else:
        msg = '\033[31mVocê perdeu pois PAPEL embrulha PEDRA\033[m'
elif escolhaJogador == 2: 
    if escolhaComputador == 3:
        msg = '\033[31mVocê perdeu pois TESOURA corta PAPEL\033[m'
    elif escolhaComputador == 2:
        msg = '\033[33mEMPATE\033[m'
    else:
        msg = '\033[32mVocê ganhou pois PAPEL embrulha PEDRA\033[m'
elif escolhaJogador == 3: 
    if escolhaComputador == 1:
        msg = '\033[31mVocê perdeu pois PEDRA amassa a TESOURA\033[m'
    elif escolhaComputador == 3:
        msg = '\033[33mEMPATE\033[m'
    else:
        msg = '\033[32mVocê ganhou pois TESOURA corta o PAPEL\033[m'
else:
    print('Jogada inválida')
    exit()

print('Você escolheu {} e o coputador escolheu {}'.format(escolhasPossiveis[escolhaJogador], escolhasPossiveis[escolhaComputador]))

print(msg)