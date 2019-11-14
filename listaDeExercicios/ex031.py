# coding=UTF-8
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas

distancia = int(input('Digite a distância da viagem em Km: '))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print('O valor da passagem é {:.2f}'.format(passagem))