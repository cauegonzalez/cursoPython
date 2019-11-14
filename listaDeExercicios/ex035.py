# coding=UTF-8
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

reta1 = int(input('Digite o comprimento da 1ª reta: '))
reta2 = int(input('Digite o comprimento da 2ª reta: '))
reta3 = int(input('Digite o comprimento da 3ª reta: '))
possivel = True

if possivel and (reta1 > reta3 + reta2):
#     possivel = True
# else:
    possivel = False
        
if possivel and (reta3 > reta1 + reta2):
#     possivel = True
# else:
    possivel = False

if possivel and (reta2 > reta3 + reta1):
#     possivel = True
# else:
    possivel = False

print('')
if possivel:
    print('Os comprimentos informados permitem que seja formado um triângulo')
else:
    print('Os comprimentos informados NÃO permitem que seja formado um triângulo')