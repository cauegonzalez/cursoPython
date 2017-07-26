# Crie um programa que leia um número e mostre na tela seu dobro, triplo e raiz quadrada
valor1 = int(input('Digite um valor: '))
dobro  = valor1 * 2
triplo = valor1 * 3
raiz   = valor1 ** (1/2)

print('O dobro de {} é: {}'.format(valor1, dobro))
print('O triplo de {} é: {}'.format(valor1, triplo))
print('A raiz quadrada de {} é: {}'.format(valor1, raiz))
