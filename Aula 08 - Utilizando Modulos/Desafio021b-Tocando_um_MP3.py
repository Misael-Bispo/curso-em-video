import pygame

pygame.mixer.init()
pygame.mixer.music.load('papo-de-undaia.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
# Mantém o script rodando para o áudio tocar até você encerrar
input('Pressione ENTER para parar a música...')
