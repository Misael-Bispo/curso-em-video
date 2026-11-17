from random import randint
from time import sleep

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
nu = int(input('Em que número pensei? '))
nm = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if nu == nm:
    print(f'Parabéns! Você conseguiu me vencer! Eu pensei no número {nm} também!')
else:
    print(f'Ganhei! Eu pensei no número {nm} e não no {nu}!')
