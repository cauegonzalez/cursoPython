# coding=UTF-8
# Trabalhando com Listas compostas
print('====Exercício Aula 19====')

# dados = dict()
# dados = { 'nome': 'Pedro', 'idade': 25}
# print(dados['nome'])
# print(dados['idade'])
# print(dados.values())
# print(dados.keys())
# print(dados.items())

pessoas = {'nome': 'Cauê', 'sexo': 'M', 'idade': 34}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['peso'] = 99
del pessoas['sexo']
for key, value in pessoas.items():
    print(f'{key} = {value}')

print('-' * 30)
estado = {}
pais = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    pais.append(estado.copy())

for e in pais:
    for key, value in e.items():
        print(f'O campo {key.upper()} tem valor {value}.')