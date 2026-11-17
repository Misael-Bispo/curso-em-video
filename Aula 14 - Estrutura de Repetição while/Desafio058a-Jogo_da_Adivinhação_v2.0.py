from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi?''')
computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        else:
            print('Menos... Tente mais uma vez. ')

print(f'Acertou em {palpites} tentativas. Parabéns')

