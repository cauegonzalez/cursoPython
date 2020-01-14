# coding=UTF-8
# Trabalhando com Listas
print('====Exercício Aula 17====')

lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']
print(lanche)
# insere no final
lanche.append('Cookie')
print(lanche)
# insere no índice indicado
lanche.insert(0, 'Cachorro-quente')
print(lanche)

# exclui o elemento indicado
del lanche[4]
print(lanche)

# pop exclui o último, ou se passado o parâmetro, exclui o valor do índice informado
lanche.pop(2)
print(lanche)

# remove o item com o valor indicado
if 'Cookie' in lanche:
    lanche.remove('Cookie')
print(lanche)

print(len(lanche))

valores = list(range(4,15))
print(valores)
    
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
    
print(sorted(lanche))
print(lanche)
print(lanche[2])
print(lanche[1:3])
print(lanche[-3])
print(lanche[-3:])
print(lanche[2:])
print(lanche[:2])

exit()

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
