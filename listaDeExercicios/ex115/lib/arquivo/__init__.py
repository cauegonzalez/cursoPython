from lib.interface import *

def arquivoExiste(nome):
    '''
    -> Função que verifica se um arquivo existe
    :param nome: caminho do arquivo a ser verificado
    :return: boolean
    '''
    try:
        a = open(nome, 'rt')
        a.close() 
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    '''
    -> Função que cria um arquivo
    :param nome: caminho do arquivo a ser criado
    '''
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    '''
    -> Função para ler um arquivo texto
    :param nome: caminho do arquivo a ser lido
    '''
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        lista = a.readlines()
        for pessoa in lista:
            nome, idade = pessoa.replace('\n', '').split(';')
            print(f'{nome:<30}', end='')
            print(f'{idade:>6}', end='')
            print(' anos.')
    finally:
        a.close


def cadastrar(nomeArquivo, nome='desconhecido', idade=0):
    '''
    -> Função que cadastra uma pessoa no arquivo
    :param nomeArquivo: caminho do arquivo que a pessoa será cadastrada
    :param nome: nome da pessoa que está sendo cadastrada
    :param idade: idade da pessoa que está sendo cadastrada
    '''
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
    finally:
        a.close()
