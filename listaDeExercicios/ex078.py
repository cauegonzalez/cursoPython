# coding=UTF-8
# Faça um programa leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valro digitado e as suas respectivas posições na lista

lista = list()
menores = list()
maiores = list()
for n in range(0, 5):
    lista.append(int(input('Digite um valor inteiro: ')))

menor = min(lista)
maior = max(lista)
for chave, n in enumerate(lista):
    if n == menor:
        menores.append(chave)
    if n == maior:
        maiores.append(chave)

print(f'Você digitou a lista: {lista}')
print(f'O maior valor é o {maior}, encontrado nas posições: {maiores}')
print(f'O menor valor é o {menor}, encontrado nas posições: {menores}')
