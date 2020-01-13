# coding=UTF-8
# Crie uma tupla preenchida com a classificação do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# - Apenas os 8 primeiros colocados
# - Os últimos 4 colocados da tabela
# - Uma lista com os times em ordem alfabética
# - Em que posição na tabela está o time da Chapecoense

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Os 8 times classificados para a libertadores são: \n\t{times[0:8]}')
print(f'Os 4 times rebaixados para a segunda divisão são: \n\t{times[-4:]}')
print(f'Os times em ordem alfabética são:\n\t{sorted(times)}')
print(f'O time da Chapecoense terminou o campeonato na {times.index("Chapecoense") + 1}ª posição.')