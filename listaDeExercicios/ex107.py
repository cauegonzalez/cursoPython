# coding=UTF-8
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# 
# Faça também um programa que importe esse módulo e use algumas dessas funções
import ex107moeda

numero = int(input('Digite um número para ser aumentado em 10%: '))
maior = ex107moeda.aumentar(numero)
print(f'O número digitado foi {numero} e após ser aumentado ficou {maior}.')

numero = int(input('Digite um número para ser diminuído em 15%: '))
menor = ex107moeda.diminuir(numero)
print(f'O número digitado foi {numero} e após ser diminuído ficou {menor}.')

numero = int(input('Digite um número para ser dobrado: '))
dobro = ex107moeda.dobro(numero)
print(f'O número digitado foi {numero} e após ser dobrado ficou {dobro}.')

numero = int(input('Digite um número para ser reduzido pela metade: '))
metade = ex107moeda.metade(numero)
print(f'O número digitado foi {numero} e após ser reduzido pela metade ficou {metade}.')