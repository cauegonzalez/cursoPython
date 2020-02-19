def aumentar(numero, formatar = False):
    if formatar:
        return moeda(numero * 1.1)
    return numero * 1.1


def diminuir(numero, formatar = False):
    if formatar:
        return moeda(numero - numero * 0.15)
    return numero - numero * 0.15


def dobro(numero, formatar = False):
    if formatar:
        return moeda(numero * 2)
    return numero * 2


def metade(numero, formatar = False):
    if formatar:
        return moeda(numero / 2)
    return numero / 2


def moeda(numero):
    return f'R$ {numero:.2f}'.replace('.', ',')
    