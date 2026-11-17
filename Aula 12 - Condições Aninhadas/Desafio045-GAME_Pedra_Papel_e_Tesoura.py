from random import randint
from time import sleep

print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
nu = int(input('Qual é a sua jogada? '))
nm = randint(0, 2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 11)
print(f'Jogador jogou {lista[nu]}')
print(f'Computador jogou {lista[nm]}')
print('-=' * 11)

if nu == 0:
    if nm == 0:
        print('EMPATE')
    elif nm == 1:
        print('COMPUTADOR VENCE')
    elif nm == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif nu == 1:
    if nm == 0:
        print('JOGADOR VENCE')
    elif nm == 1:
        print('EMPATE')
    elif nm == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif nu == 2:
    if nm == 0:
        print('COMPUTADOR VENCE')
    elif nm == 1:
        print('JOGADOR VENCE')
    elif nm == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

