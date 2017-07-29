# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))

# as funções que este programa executa exige que o parâmetro seja passado em radianos
anguloRad = radians(angulo)

seno = sin(anguloRad)
cosseno = cos(anguloRad)
tangente = tan(anguloRad)

print('O ângulo {:.2f}º possui seno igual a {:.2f}.'.format(angulo, seno))
print('O ângulo {:.2f}º possui cosseno igual a {:.2f}.'.format(angulo, cosseno))
print('O ângulo {:.2f}º possui tangente igual a {:.2f}.'.format(angulo, tangente))
