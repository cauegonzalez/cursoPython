# coding=UTF-8
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER.
# Deve mostrar na tela o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

contador = 0
while True:
    print('=-' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 30)
    jogador = int(input('Digite valor: '))
    computador = randint(0, 10)
    escolhaJogador = ' '
    while escolhaJogador not in 'PI':
        escolhaJogador = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    soma = jogador + computador
    
    if soma % 2 == 0:
        resultado = 'P'
        resultadoExtenso = 'PAR'
    else:
        resultado = 'I'
        resultadoExtenso = 'ÍMPAR'
        
    print('--' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}, deu {resultadoExtenso}')
    print('--' * 30)

    if escolhaJogador == resultado:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        contador += 1
    else:
        print('Você PERDEU!')
        break
print('=-' * 30)
print(f'GAME OVER! Você venceu {contador} vezes.')