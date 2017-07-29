# Crie um programa que leia uma temperatura em Celcius e converta para Farenheit
temperaturaC = float(input('Digite a temperatura em ºC: '))
temperaturaF = ((9 * temperaturaC) / 5) + 32

print('A temperatura de {}ºC corresponde a {}ºF.'.format(temperaturaC, temperaturaF))
