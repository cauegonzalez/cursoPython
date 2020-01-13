# coding=UTF-8
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do programa

operador1 = int(input('Digite um número: '))
operador2 = int(input('Digite outro número: '))

operacao = -1

while operacao != 5:
    print('O que deseja fazer?')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do programa')
    operacao  = int(input('Digite o número correspondente à operação desejada: '))
    
    if operacao == 1:
        print('A soma de {} + {} = {}\n'.format(operador1, operador2, operador1 + operador2))
    elif operacao == 2:
        print('A multiplicação de {} * {} = {}\n'.format(operador1, operador2, operador1 * operador2))
    elif operacao == 3:
        if operador1 > operador2:
            print('Entre {} e {}, o maior é {}\n'.format(operador1, operador2, operador1))
        else:
            print('Entre {} e {}, o maior é {}\n'.format(operador1, operador2, operador2))
    elif operacao == 4:
        print('===' * 10)
        operador1 = int(input('Digite um número: '))
        operador2 = int(input('Digite outro número: '))
    elif operacao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente.')
    print('===' * 10, end='\n\n')
print('Fim do programa! Volte sempre!')