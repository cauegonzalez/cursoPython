# coding=UTF-8
# Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: 
# o primeiro é o valor a calcular e o outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial
def fatorial(n, show=True):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: o valor do Fatorial de um número n.
    """
    f = 1
    print(f'{n}! => ', end='')
    for i in range(n, 1, -1):
        if show:
            print(f'{i}', end='')
            if i > 2:
                print(' x ', end='')
            else:
                print(' x 1 = ', end='')
        f *= i
    return f


# help(fatorial)

n = int(input('Digite o número para cálculo do fatorial: '))
while True:
    show = str(input('Mostrar? [S/N] ')).strip().upper()[0]
    if show in 'SN':
        break
show = True if show == 'S' else False
print(fatorial(n, show))