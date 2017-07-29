# Crie um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado
distancia = float(input('Digite quantos Km foram rodados: '))
dias = int(input('Digite a quantidade de dias em que o carro permaneceu alugado: '))

valorPagar = 60 * dias + distancia * 0.15

print('O valor total a ser pago pelo aluguel do carro é R$ {:.2f}'.format(valorPagar))
