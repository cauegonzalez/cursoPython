# Crie um programa que receba dois números, apresente seus tipos primitivos e ainda mostre a soma entre os dois.
print('====Exercício Aula 06====')
valor1  = float(input('Digite um valor: '))
print('O tipo digitado é:', type(valor1))
valor2  = float(input('Digite outro valor: '))
print('O tipo digitado é:', type(valor2))
print('---------------------------')
# print('A soma entre',valor1,'e',valor2,'é:',valor1+valor2) <-- sintaxe antiga
print('A soma entre {0} e {1} é: {2}'.format(valor1,valor2, valor1+valor2))
