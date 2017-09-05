# Crie um programa que execute as diversas funcionalidades vistas em aula aplicadas a strings
print('====Exercício Aula 09====')
frase = '    Curso em vídeo Python   '
print('mostra o tamanho da string: {}'.format(len(frase)))
print('mostra o tamanho da string retirando espaços do início e do fim: {}'.format(len(frase.strip())))
# alterando o conteúdo da variável para demais exemplos
frase = 'Curso em vídeo Python'
print('string inteira: {}'.format(frase))
print('apenas o caractere 3: {}'.format(frase[3]))
print('inicia no caractere 3 e finaliza no 8: {}'.format(frase[3:9]))
print('inicia no início e finaliza no caractere 8: {}'.format(frase[:9]))
print('inicia no caractere 3, finaliza no 9 e pula 2 a cada impressão: {}'.format(frase[3:9:2]))
print('inicia no caractere 3 e finaliza no fim da string: {}'.format(frase[3:]))
print('inicia no caractere 3, finaliza no fim, pulando 3 a cada impressão: {}'.format(frase[3::3]))
print('inicia no início, finaliza no fim, pulando 2 a cada impressão: {}'.format(frase[::2]))
print('conta quantos caracteres especificados existem: {}'.format(frase.count('o')))
print('conta quantos caracteres especificados existem ignorando o case sensitive: {}'.format(frase.upper().count('O')))
print('substituir algo na string: {}'.format(frase.replace('Python', 'Android')))
print('verifica se uma determinada substring está contida na string: {}'.format('Curso' in frase))
print('indica a primeira posição de uma substring: {}'.format(frase.find('vídeo')))
print('indica a primeira posição de uma substring (-1 se não encontrar (case sensitive)): {}'.format(frase.find('Vídeo')))
print('indica a primeira posição de uma substring (ignorando o case sensitive): {}'.format(frase.lower().find('curso')))
dividido = frase.split()
print('imprimir a string splitada: {}'.format(dividido))
print('imprimir somente uma posição da string splitada: {}'.format(dividido[3]))
print('imprimir somente uma letra de uma posição da string splitada: {}'.format(dividido[3][3]))
print('imprimir a frase da variável dividido utilizando outro caractere como separador: {}'.format('_'.join(dividido)))
# para imprimir várias linhas, considerando suas quebras, utilizar texto entre 3 aspas duplas
print("""
Aqui vai um texto mais completo
utilizando mais de uma linha e aplicando o conceito de
envolver o texto todo em 3 conjuntos de aspas duplas""")