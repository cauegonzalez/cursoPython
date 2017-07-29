# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
import math
real = float(input('Digite um número real: '))

inteiro = math.trunc(real)
inteiro2 = math.floor(real)

print('O número {} tem a parte inteira {}'.format(real, inteiro))
print('O número {} tem a parte inteira {}'.format(real, inteiro2))
