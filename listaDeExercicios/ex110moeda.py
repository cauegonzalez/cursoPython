def aumentar(numero, percentualAumento, formatar = False):
    novoValor = numero + (numero * percentualAumento / 100)
    if formatar:
        return moeda(novoValor)
    return novoValor


def diminuir(numero, percentualDesconto, formatar = False):
    novoValor = numero - (numero * percentualDesconto / 100)
    if formatar:
        return moeda(novoValor)
    return novoValor


def dobro(numero, formatar = False):
    if formatar:
        return moeda(numero * 2)
    return numero * 2


def metade(numero, formatar = False):
    if formatar:
        return moeda(numero / 2)
    return numero / 2


def moeda(numero):
    return f'R$ {numero:.2f}'


def resumo(preco, percentualAumento, percentualDesconto):
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
