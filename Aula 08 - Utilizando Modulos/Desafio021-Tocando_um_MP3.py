import pygame

# Inicializa o mixer e carrega o arquivo de áudio
pygame.mixer.init()
pygame.mixer.music.load('papo-de-undaia.mp3')  # Certifique-se de que o arquivo está na mesma pasta

# Inicia a reprodução
pygame.mixer.music.play()

# Mantém o script rodando para o áudio tocar até você encerrar
input('Pressione ENTER para parar a música...')
