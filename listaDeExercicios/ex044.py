# coding=UTF-8
# Elaboreum programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço Normal
# 3x ou mais no cartão: 20% de juros

print('{:=^50}'.format(' LOJAS GONZALEZ '))

preco = float(input('Digite o preço do produto: '))
formaPagamento = int(input("""Escolha uma forma de pagamento:
    - [ 1 ]: à vista (dinheiro/cheque)
    - [ 2 ]: à vista (cartão)
    - [ 3 ]: até 2x no cartão
    - [ 4 ]: 3x ou mais no cartão
"""))

if formaPagamento == 1:
    desconto = preco * 0.1
    juros = 0
elif formaPagamento == 2:
    desconto = preco * 0.05
    juros = 0
elif formaPagamento == 3:
    desconto = 0
    juros = 0
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R$ {} sem juros'.format(parcela))
elif formaPagamento == 4:
    desconto = 0
    juros = preco * 0.2
    qtdeParcelas = int(input('Escolha a quantidade de parcelas: '))
    parcela = (preco + juros) / qtdeParcelas
    print('Sua compra será parcelada em {}x de R$ {} com juros'.format(qtdeParcelas, parcela))
else:
    print('Opção inválida')
    exit()

precoFinal = preco - desconto + juros
print('O preço final a ser pago pelo produto é R$ \033[37;44m{:.2f}\033[m, considerando R$ {:.2f} de desconto e R$ {:.2f} de juros.'.format(precoFinal, desconto, juros))