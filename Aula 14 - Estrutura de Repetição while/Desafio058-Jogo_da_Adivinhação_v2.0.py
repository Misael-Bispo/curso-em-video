from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi?''')
nm = randint(0, 10)
nu = int(input('Qual é o seu palpite? '))
cont = 0

while nm != nu:
    if nu > nm:
        print('Menos... Tente mais uma vez. ')
    else:
        print('Mais... Tente mais uma vez. ')
    nu = int(input('Qual é o seu palpite? '))
    cont += 1

print(f'Acertou em {cont} tentativas. Parabéns')
