# Crie um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Digite o preço do produto: '))

novoPreco = preco - (preco * (5 / 100))
print('O produto está em promoção de: R$ {:.2f} por R$ {:.2f}.'.format(preco, novoPreco))
