# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = float(input('Digite a distância em metros: '))
centimetros = valor * 100
milímetros = valor * 1000

print('A distância {} equivale a {} centímetros ou {} milímetros.'.format(valor, centimetros, milímetros))
