# coding=UTF-8
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = './pessoas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arquivo)
    elif opcao == 2:
        # Opção de cadastrar a pessoa em um arquivo!
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif opcao == 3:
        # Opção de sair do sistema!
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[031mERRO: Digite uma opção válida!\033[m')
    sleep(2)
