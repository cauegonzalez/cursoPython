def leiaDinheiro(msg):
    """
    -> Espera receber um valor monetário pelo teclado informando a mensagem recebida por parâmetro
    :param msg: mensagem
    :return: o valor monetário informado
    """
    while True:
        numero = str(input(msg)).strip().replace(',', '.')
        
        try:
            n = float(numero)
            return n 
        except:
            print(f'\033[31mERRO: "{numero}" é um preço inválido!\033[m')


def leia_int(msg):
    """
    -> Espera receber um valor inteiro pelo teclado informando a mensagem recebida por parâmetro
    :param msg: mensagem
    :return: o inteiro informado
    """
    n = str(input(msg))
    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um número inteiro válido\033[m') 
        n = str(input(msg))

    return n
