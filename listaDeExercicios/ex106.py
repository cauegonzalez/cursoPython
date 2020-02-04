# coding=UTF-8
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM' o programa encerrará.
# OBS.: use cores
from time import sleep

def linha(char, tamanho):
    print(char * tamanho)


def cabecalho(msg, flush=False):
    tamanho = len(msg) + 4
    linha('~', tamanho)
    print(f'{msg:^{tamanho}}', flush=flush)
    linha('~', tamanho)


def show_help(funcao):
    print(f'{cores["fundoRoxo"]}', end='')
    cabecalho(f'Acessando o manual do comando \'{funcao}\'', flush=True)
    print(f'{cores["limpa"]}', end='')
    sleep(1)
    print(f'{cores["fundoBranco"]}', end='')
    help(funcao)
    print(f'{cores["limpa"]}', end='')


# Programa Principal
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    'normal': '\033[0m',
    'bold': '\033[1m',
    'underlined': '\033[4m',
    'pretoebranco': '\033[7;37m',
    'fundoVermelho': '\033[0;30;41',
    'fundoVerde': '\033[0;30;42m',
    'fundoAmarelo': '\033[0;30;43m',
    'fundoAzul': '\033[0;30;44m',
    'fundoRoxo': '\033[0;30;45m',
    'fundoBranco': '\033[7;30m'
}

print(f'{cores["fundoVerde"]}', end='')
cabecalho('SISTEMA DE AJUDA PyHELP')
print(f'{cores["limpa"]}', end='')
while True:
    funcao = str(input('Função ou Biblioteca > '))
    if funcao.upper() == 'FIM':
        break
    show_help(funcao)