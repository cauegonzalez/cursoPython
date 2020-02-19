# coding=UTF-8
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas 
# vai ser ou não formatado pela função moeda() desenvolvida no desafio 108
import ex109moeda

numero = float(input('Digite um valor para ser aumentado em 10%: '))
maior = ex109moeda.aumentar(numero, True)
print(f'O número digitado foi {ex109moeda.moeda(numero)} e após ser aumentado ficou {maior}.')

numero = int(input('Digite um número para ser diminuído em 15%: '))
menor = ex109moeda.diminuir(numero, True)
print(f'O número digitado foi {ex109moeda.moeda(numero)} e após ser diminuído ficou {menor}.')

numero = int(input('Digite um número para ser dobrado: '))
dobro = ex109moeda.dobro(numero, True)
print(f'O número digitado foi {ex109moeda.moeda(numero)} e após ser dobrado ficou {dobro}.')

numero = int(input('Digite um número para ser reduzido pela metade: '))
metade = ex109moeda.metade(numero, True)
print(f'O número digitado foi {ex109moeda.moeda(numero)} e após ser reduzido pela metade ficou {metade}.')