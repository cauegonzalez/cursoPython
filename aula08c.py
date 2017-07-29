"""
Crie um programa que imprima uma mensagem seguida de um emoji
ps.: so esta funcionando no python2
"""
import emoji
print('====Exercicio Aula 08====')
msg = emoji.emojize("Hello world :earth_americas:", use_aliases=True)
print(msg)
