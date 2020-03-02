def leiaInt(msg):
    '''
    -> Função criada para ler um número inteiro e não aceitar algo diferente
    :param msg: mensagem a ser exibida no comando a esperar a leitura do número
    :return: valor inteiro digitado
    '''
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31m\nForçando o encerramento do sistema!\033[m')
            exit()
        except:
            print('\033[31mERRO: O número digitado não é um inteiro válido!\033[m')
        else:
            return inteiro


def leiaFloat(msg):
    '''
    -> Função criada para ler um número real e não aceitar algo diferente
    :param msg: mensagem a ser exibida no comando a esperar a leitura do número
    :return: valor real digitado
    '''
    while True:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31m\nForçando o encerramento do sistema!\033[m')
            exit()
        except:
            print('\033[31mERRO: O número digitado não é um número real válido!\033[m')
        else:
            return real


def linha(tamanho=42):
    '''
    -> Função que retorna uma linha de acordo com o tamanho especificado
    :param tamanho: tamanho da linha a ser criada
    :return: linha do tamanho especificado
    '''
    return '-' * tamanho


def cabecalho(msg, tamanho=42):
    '''
    -> Função que apresenta um cabeçalho de acordo com a mensagem e o tamanho especificado
    :param msg: mensagem do cabeçalho
    :param tamanho: tamanho a ser considerado para o cabeçalho
    '''
    print(linha(tamanho))
    print(msg.center(tamanho))
    print(linha(tamanho))


def menu(list):
    '''
    -> Função que apresenta um menu com as opções recebidas por parâmetro
    :param list: lista com as opções que devem ser disponibilizadas
    :return: opção escolhida pelo usuário
    '''
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in list:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print(linha())
    opcao = leiaInt('\033[32mSua Opção:\033[m ')
    return opcao
