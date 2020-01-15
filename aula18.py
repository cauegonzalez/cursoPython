# coding=UTF-8
# Trabalhando com Listas compostas
print('====Exercício Aula 18====')

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[2])
print(galera[3][0])

print('--' * 30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('--' * 30)
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
    
totalMaior = totalMenor = 0
for p in galera:
    if p[1] >= 21:
        totalMaior += 1
        print(f'{p[0]} é maior de idade')
    else:
        totalMenor += 1
        print(f'{p[0]} é menor de idade')
print(f'Temos {totalMaior} pessoas maior de idade e {totalMenor} pessoas menor de idade.')
    