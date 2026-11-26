from random import randint
import time

jogos = list()
temp = []

print('-=' * 25)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-=' * 25)

n = int(input(f'Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= n:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    tot += 1

print('-=' *7, f'SORTEANDO {n} JOGOS', '-=' *7)
time.sleep(0.5)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(0.5)

print('-=' *9, f'BOA SORTE!', '-=' *9)