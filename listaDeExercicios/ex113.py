# coding=UTF-8
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31m\nERRO: O usuário preferiu não informar dados!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: O número digitado não é um inteiro válido!\033[m')
        else:
            return inteiro

    
def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31m\nERRO: O usuário preferiu não informar dados!\033[m')
            return float(0)
        except (ValueError, TypeError):
            print('\033[31mERRO: O número digitado não é um número real válido!\033[m')
        else:
            return real
    
    
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {inteiro} e o número real foi {real}')