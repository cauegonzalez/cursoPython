# coding=UTF-8
# Trabalhando com Tuplas
print('====Exercício Aula 16====')
# Tuplas são IMUTÁVEIS
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(sorted(lanche))
print(lanche[2])
print(lanche[1:3])
print(lanche[-3])
print(lanche[-3:])
print(lanche[2:])
print(lanche[:2])

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print('Comi pra caramba!')

print('==' * 30)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(c)
print(c.count(5))
print(c.index(8))
