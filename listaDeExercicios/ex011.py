# Crie um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Digite a largura da parede: '))
altura  = float(input('Digite a altura da parede: '))

area = largura * altura
litros = area / 2
print('Sua parede tem {:.2f} m², então é necessário utilizar {:.2f} litros de tinta'.format(area, litros))
