# Escreva um programa em Python que abra e reproduza o audio de um arquivo mp3
# importacao de modulo externo funcionou apenas no python 2. e sem aceitar caracteres especiais. nem nos comentarios
import pygame
pygame.init()
file = 'ex021.mp3'

pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
