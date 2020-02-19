def aumentar(numero, percentualAumento, formatar=False):
    """
    -> Recebe um valor e aplica um percentual de aumento de acordo com o parâmetro recebido. Permite ainda informar se deve devolver já formatado ou não
    :param numero: valor a ser trabalhado
    :param percentualAumento: total do percentual que deve ser aplicado em cima do valor informado
    :param formatar: booleano que indica se deve ou não retornar o valor com a formatação de moeda
    :return: valor já com o aumento indicado
    """
    novoValor = numero + (numero * percentualAumento / 100)
    if formatar:
        return moeda(novoValor)
    return novoValor


def diminuir(numero, percentualDesconto, formatar=False):
    """
    -> Recebe um valor e aplica um percentual de desconto de acordo com o parâmetro recebido. Permite ainda informar se deve devolver já formatado ou não
    :param numero: valor a ser trabalhado
    :param percentualDesconto: total do percentual de desconto que deve ser aplicado em cima do valor informado
    :param formatar: booleano que indica se deve ou não retornar o valor com a formatação de moeda
    :return: valor já com o desconto indicado
    """
    novoValor = numero - (numero * percentualDesconto / 100)
    if formatar:
        return moeda(novoValor)
    return novoValor


def dobro(numero, formatar=False):
    """
    -> Recebe um valor e devolve o dobro. Permite ainda informar se deve devolver já formatado ou não
    :param numero: valor a ser trabalhado
    :param formatar: booleano que indica se deve ou não retornar o valor com a formatação de moeda
    :return: dobro do valor recebido
    """
    if formatar:
        return moeda(numero * 2)
    return numero * 2


def metade(numero, formatar=False):
    """
    -> Recebe um valor e devolve a metade. Permite ainda informar se deve devolver já formatado ou não
    :param numero: valor a ser trabalhado
    :param formatar: booleano que indica se deve ou não retornar o valor com a formatação de moeda
    :return: metade do valor recebido
    """
    if formatar:
        return moeda(numero / 2)
    return numero / 2


def moeda(numero):
    """
    -> Recebe um valor e devolve o mesmo formatado como moeda brasileira (R$)
    :param numero: valor a ser trabalhado
    :return: valor com a formatação de moeda brasileira (R$)
    """
    return f'R$ {numero:.2f}'.replace('.', ',')


def resumo(preco, percentualAumento, percentualDesconto):
    """
    -> Recebe um valor e seus percentuais de aumento e de desconto e apresenta um resumo dos valores aplicando cada uma das funções disponíveis
    :param preco: valor a ser trabalhado
    :param percentualAumento: necessário para chamar a função aumentar()
    :param percentualDesconto: necessário para chamar a função diminuir()
    """
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    maior = aumentar(preco, percentualAumento, True)
    menor = diminuir(preco, percentualDesconto, True)
    dobrado = dobro(preco, True)
    valorMetade = metade(preco, True)
    print(f'{"Preço analisado:":<30}', end='')
    print(f'{moeda(preco)}')
    msg = f'Aumentado em {percentualAumento}%:'
    print(f'{msg:<30}', end='')
    print(f'{maior}')
    msg = f'Diminuído em {percentualDesconto}%:'
    print(f'{msg:<30}', end='')
    print(f'{menor}')
    print(f'{"Dobro do preço:":<30}', end='')
    print(f'{dobrado}')
    print(f'{"Metade do preço:":<30}', end='')
    print(f'{valorMetade}')
    print('-'*40)
