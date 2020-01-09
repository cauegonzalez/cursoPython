# coding=UTF-8
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - A média de idade do grupo
# - O nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

somatorioIdade = 0
idadeMaior = 0
nomeHomemMaisVelho = '' 
quantidadeMulheresMenosVinte = 0
contador = 0
for i in range(1, 5):
    contador += 1
    print('_____{}ª PESSOA_____'.format(i))
    nome = input('Nome: '.format(i)).strip()
    idade = int(input('Idade: '.format(i)))
    sexo = input('Sexo [M/F]: '.format(i)).strip().upper()

    somatorioIdade += idade 
    if sexo == 'M': 
        if idade > idadeMaior:
            idadeMaior = idade
            nomeHomemMaisVelho = nome
    else:
        if idade < 20:
            quantidadeMulheresMenosVinte += 1 
media = somatorioIdade / contador

print("""A média de idade do grupo é '{}'
O homem mais velho é o {}, com {} anos.
A quantidade de mulheres com menos de 20 anos é {}.""".format(media, nomeHomemMaisVelho, int(idadeMaior), quantidadeMulheresMenosVinte))
