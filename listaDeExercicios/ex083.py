# coding=UTF-8
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expressao = str(input('Digite uma expressão que utilize parênteses: '))
tamanho = len(expressao)
pilha = []
for i in range(0, tamanho):
    if expressao[i] == '(':
        pilha.append('(')
    elif expressao[i] == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print(f'A expressão {expressao} está CORRETA!')
else:
    print(f'A expressão {expressao} está INCORRETA!')
    print(f'A pilha restante foi {pilha}')