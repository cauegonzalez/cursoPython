# coding=UTF-8
# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lita ordenada (sem usar o sort()).
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = list()
for i in range(0, 5):
    aux = int(input('Digite um valor inteiro: '))
    if i == 0 or aux > valores[-1]:
        valores.append(aux)
    else:
        for j, valor in enumerate(valores):
            if aux < valor:
                inseriu = True
                valores.insert(j, aux)
                break
print('Você digitou a lista: {}'.format(valores))
