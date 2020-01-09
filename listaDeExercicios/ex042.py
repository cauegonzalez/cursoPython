# coding=UTF-8
# Refaçao desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

reta1 = int(input('Digite o comprimento da 1ª reta: '))
reta2 = int(input('Digite o comprimento da 2ª reta: '))
reta3 = int(input('Digite o comprimento da 3ª reta: '))
possivel = True

if possivel and (reta1 > reta3 + reta2):
    possivel = False
        
if possivel and (reta3 > reta1 + reta2):
    possivel = False

if possivel and (reta2 > reta3 + reta1):
    possivel = False

print('')
if possivel:
    if reta1 == reta2 == reta3:
        tipoTriangulo = 'EQUILÁTERO'
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        tipoTriangulo = 'ISÓSCELES'
    else:
        tipoTriangulo = 'ESCALENO'
    print('Os comprimentos informados permitem que seja formado um triângulo \033[36m{}\033[m'.format(tipoTriangulo))
else:
    print('Os comprimentos informados NÃO permitem que seja formado um triângulo')