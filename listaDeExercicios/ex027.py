# Faça um programa que leia o nome completo de uma pessoa e mostre separadamente o primeiro e o último nome
#
pessoa = input('Digite o nome completo de uma pessoa: ')

print('Nome digitado: {}'.format(pessoa))
nome = pessoa.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome) -1]))