# coding=UTF-8
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('aprender', 
            'programar', 
            'linguagem', 
            'python', 
            'curso', 
            'gratis', 
            'estudar', 
            'praticar', 
            'trabalhar', 
            'mercado', 
            'programador', 
            'KGB', 
            'futuro')

print('')
for palavra in palavras:
    resposta = ''
    for letra in palavra.upper():
        if letra in 'AEIOU':
            resposta += letra + ' '
    if len(resposta) > 0:
        print(f'Na palavra {palavra.upper()} temos {resposta.lower()}') 
    else:
        print(f'Na palavra {palavra.upper()} não possui vogais')

print('\nFIM do PROGRAMA')
