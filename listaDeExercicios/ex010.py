# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerar US$1,00 = R$ 3,27
valor = float(input('Digite quanto você possui na carteira: '))

print('Com R$ {:.2f} é possível comprar US$ {:.2f} e sobram R$ {:.2f}'.format(valor, valor // 3.27, valor % 3.27))
