# coding=UTF-8
# Desenvolva um programa que leia o idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar.
# No final do programa mostre:
# - Quantas pessoas tem mais de 18 anos
# - Quantos homens foram cadastrados
# - Quantas mulheres tem menos de 20 anos

quantidadePessoasMaisDezoito = quantidadeHomens = quantidadeMulheresMenosVinte = i = 0
while True:
    i += 1
    print(f'_____{i}ª PESSOA_____')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]

    if idade >= 18:
        quantidadePessoasMaisDezoito += 1

    if sexo == 'M': 
        quantidadeHomens += 1
    else:
        if idade <= 20:
            quantidadeMulheresMenosVinte += 1 
    if continuar == 'N':
        break

print(f"""A quantidade de pessoas com mais de 18 anos é {quantidadePessoasMaisDezoito}
A quantidade de homens cadastrados foi {quantidadeHomens}.
A quantidade de mulheres com menos de 20 anos é {quantidadeMulheresMenosVinte}.""")
