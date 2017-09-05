# Faça um programa que leia uma frase pelo teclado e mostre:
#    - Quantas vezes aparece a letra A
#    - Em que posição ela aparece pela primeira vez
#    - Em que posição ela aparece pela última vez
#
frase = input('Digite uma frase: ')

quantidadeA = frase.upper().count('A')
posicaoPrimeiroA = frase.upper().find('A')
posicaoUltimoA = frase.upper().rfind('A')
print("""A frase '{}'
Possui {} letras A.
A primeira posição de uma letra A é {}.
A última posição de uma letra A é {}""".format(frase, quantidadeA, posicaoPrimeiroA, posicaoUltimoA))