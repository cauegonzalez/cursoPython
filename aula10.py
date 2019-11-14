# coding=UTF-8
# Crie um programa que calcule a média conforme as duas notas digitadas
print('====Exercício Aula 10====')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 60:
    print('Parabéns, você passou de ano com média {:.2f}!'.format(media))
else:
    print('Você reprovou, sua média foi {:.2f}. Tente novamente!'.format(media))
print('--FIM--')
