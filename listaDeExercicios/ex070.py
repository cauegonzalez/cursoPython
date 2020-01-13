# coding=UTF-8
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final do programa mostre:
# - Qual é o total gasto na compra
# - Quantos produtos custam mais de R$ 1000
# - Qual é o nome do produto mais barato

total = precoMaisBaixo = quantidadeMaisDeMil = i = 0
nomeMaisBarato = ''

while True:
    i += 1
    print(f'_____{i}ª PRODUTO_____')
    nome = str(input('Nome produto: '))
    preco = float(input('Preço (R$) : '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]

    total += preco 
    if preco > 1000:
        quantidadeMaisDeMil += 1
    
    if preco < precoMaisBaixo or i == 1:
        precoMaisBaixo = preco
        nomeMaisBarato = nome
    
    if continuar == 'N':
        break

print(f"""O total gasto na compra é R$ {total:.2f}
A quantidade de produtos que custam mais de R$ 1000.00 é {quantidadeMaisDeMil}.
O produto mais barato é o produto {nomeMaisBarato} que custa R$ {precoMaisBaixo:.2f}.""")
