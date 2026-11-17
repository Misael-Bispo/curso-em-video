import pygame
import time
import threading

# Função para escutar a tecla ENTER em segundo plano
def esperar_enter():
    input('Pressione ENTER a qualquer momento para parar...\n')
    pygame.mixer.music.stop()

# Inicializa o áudio
pygame.mixer.init()
pygame.mixer.music.load('papo-de-undaia.mp3')
pygame.mixer.music.play()

# Inicia a escuta do ENTER em paralelo
thread_input = threading.Thread(target=esperar_enter, daemon=True)
thread_input.start()

# Aguarda a música terminar sozinha ou ser interrompida pelo ENTER
while pygame.mixer.music.get_busy():
    time.sleep(0.5)

print('Música encerrada!')
