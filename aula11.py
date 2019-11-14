# coding=UTF-8
# Crie um programa que utilize cores nas saídas
print('====Exercício Aula 11====')
print('\033[1;37;45mOlá Mundo!\033[m')
print('')
print('\033[7;37;45mOlá Mundo!\033[m')
print('')
print('\033[0;33;44mOlá Mundo!\033[m')
print('')
a = 3
b = 5 
print('Os valores são \033[1;41m {} \033[m e \033[1;42m {} \033[m!!!'.format(a, b))
print('')
print('Olá {}{}{}, muito prazer em te conhecer!!!'.format('\033[4;34m', 'Cauê', '\033[m'))
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
}
print('Olá {}{}{}, muito prazer em te conhecer!!!'.format(cores['pretoebranco'], 'Cauê', cores['limpa']))