# coding=UTF-8
# Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas
#   - O nome com todas as letras minúsculas
#   - Quantas letras ao todo, sem considerar espaços
#   - Quantas letras tem o primeiro nome
nomeCompleto = input('Digite o seu nome completo: ')

print('O nome digitado foi: {}'.format(nomeCompleto.upper()))
print('O nome digitado foi: {}'.format(nomeCompleto.lower()))
nomeTratado = nomeCompleto.split()
print('O nome digitado possui {} letras'.format(len(''.join(nomeTratado))))
print('O primeiro nome possui {} letras'.format(len(nomeTratado[0])))
