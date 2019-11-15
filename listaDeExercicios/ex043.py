# coding=UTF-8
# Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    status = 'Peso ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'
print('O IMC calculado foi {:.2f} e, portanto, seu status é \033[36m{}\033[m'.format(imc, status))