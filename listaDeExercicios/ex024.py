# Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
#
cidade = input('Digite o nome de uma cidade: ')

comecaComSanto = (cidade.upper().find('SANTO') == 0)
print('Cidade {} começa com Santo? {}'.format(cidade, comecaComSanto))