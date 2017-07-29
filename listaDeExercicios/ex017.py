# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
catetoAdjacente = float(input('Digite o tamanho do cateto adjacente: '))
catetoOposto = float(input('Digite o tamanho do cateto oposto: '))

hipotenusa = hypot(catetoAdjacente, catetoOposto)

print('A hipotenusa do triângulo com lados {:.2f} e {:.2f} é {:.2f}'.format(catetoAdjacente, catetoOposto, hipotenusa))
