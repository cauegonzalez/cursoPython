# coding=UTF-8
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno com dimensões {largura} x {comprimento} é {area} m²')


# programa principal
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)