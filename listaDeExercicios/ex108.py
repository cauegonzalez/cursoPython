# coding=UTF-8
# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado
import ex108moeda

numero = float(input('Digite um valor para ser aumentado em 10%: '))
maior = ex108moeda.aumentar(numero)
print(f'O número digitado foi {ex108moeda.moeda(numero)} e após ser aumentado ficou {ex108moeda.moeda(maior)}.')

numero = int(input('Digite um número para ser diminuído em 15%: '))
menor = ex108moeda.diminuir(numero)
print(f'O número digitado foi {ex108moeda.moeda(numero)} e após ser diminuído ficou {ex108moeda.moeda(menor)}.')

numero = int(input('Digite um número para ser dobrado: '))
dobro = ex108moeda.dobro(numero)
print(f'O número digitado foi {ex108moeda.moeda(numero)} e após ser dobrado ficou {ex108moeda.moeda(dobro)}.')

numero = int(input('Digite um número para ser reduzido pela metade: '))
metade = ex108moeda.metade(numero)
print(f'O número digitado foi {ex108moeda.moeda(numero)} e após ser reduzido pela metade ficou {ex108moeda.moeda(metade)}.')