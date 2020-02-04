# coding=UTF-8
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa.
# Esta função deve retornar um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(ano):
    """
    -> Função que retorna a informação se a pessoa deve votar, pode votar ou não pode votar.
    :param ano: recebe o ano de nascimento da pessoa
    :return:
    """
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    frase = f'Com {idade}: '
    if idade < 16:
        return frase + 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return frase + 'OPCIONAL'
    else:
        return frase + 'VOTO OBRIGATÓRIO'


anoNascimento = int(input('Digite o ano de nascimento: '))
print(voto(anoNascimento))