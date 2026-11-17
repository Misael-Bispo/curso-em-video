from random import randint

print(f'{'=-'*50}')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(f'{'=-'*50}')

c = 0
while True:
    n = int(input('Diga um valor: '))
    nm = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
          escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    resultado = (n + nm) % 2
    print(f'Você jogou {n} e o computador {nm}. Total de {n+nm}', end=' ')
    print('Deu PAR' if resultado == 0 else 'Deu ÍMPAR')
    print(f'{'=-'*50}')
    if escolha == 'P':
        if resultado == 0:
            print(f'Você VENCEU!')
            c += 1
        else:
            print(f'Você PERDEU!')
            break
    if escolha == 'I':
        if resultado == 1:
            print(f'Você VENCEU!')
            c += 1
        else:
            print(f'Você PERDEU!')
            break
    print(f'Vamos jogar novamente ...')
    print(f'{'=-'*50}')
print(f'GAME OVER! Você venceu {c} vezes.')
