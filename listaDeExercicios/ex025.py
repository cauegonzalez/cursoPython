# Faça um programa que leia o nome de uma pessoa e diga se ela possui ou não "SILVA" no nome
#
pessoa = input('Digite o nome de uma pessoa: ')

possuiSilva = ("SILVA" in pessoa.upper())
print('Pessoa {} possui SILVA no nome? {}'.format(pessoa, possuiSilva))