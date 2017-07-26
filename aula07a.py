# Crie um programa que rreceba dois valores e execute todos os operadores aritméticos aos mesmos
print('====Exercício Aula 07====')
valor1  = int(input('Digite um valor: '))
valor2  = int(input('Digite outro valor: '))
soma = valor1 + valor2
mult = valor1 * valor2
sub  = valor1 - valor2
div  = valor1 / valor2
divint = valor1 // valor2
mod = valor1 % valor2
pot  = valor1 ** valor2
print('-'*20)
print('A soma entre {0} e {1} é: {2}'.format(valor1,valor2, soma))
print('A multiplicação entre {0} e {1} é: {2}'.format(valor1,valor2, mult))
print('A subtração entre {0} e {1} é: {2}'.format(valor1,valor2, sub))
print('A divisão entre {0} e {1} é: {2:.3f}'.format(valor1,valor2, div))
print('A divisão inteira entre {0} e {1} é: {2}'.format(valor1,valor2, divint), end=' e ')
print('o resto da divisão entre {0} e {1} é: {2}'.format(valor1,valor2, mod))
print('A potência entre {0} e {1} é: {2}'.format(valor1,valor2, pot))
