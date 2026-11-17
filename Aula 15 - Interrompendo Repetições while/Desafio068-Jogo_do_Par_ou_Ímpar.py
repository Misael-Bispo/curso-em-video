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
    if escolha == 'P' and resultado == 0:
        print(f'{'=-'*50}')
        print(f'Você jogou {n} e o computador {nm}. Total de {n+nm} DEU PAR')
        print(f'{'=-'*50}')
        print(f'Você VENCEU!')
        print(f'Vamos jogar novamente ...')
        c += 1
    elif escolha == 'I' and resultado == 1:
        print(f'{'=-'*50}')
        print(f'Você jogou {n} e o computador {nm}. Total de {n+nm} DEU IMPAR')
        print(f'{'=-'*50}')
        print(f'Você VENCEU!')
        print(f'Vamos jogar novamente ...')
        c += 1
    elif escolha == 'P' and resultado == 1:
            print(f'{'=-'*50}')
            print(f'Você jogou {n} e o computador {nm}. Total de {n+nm} DEU IMPAR')
            print(f'{'=-'*50}')
            print(f'Você PERDEU!')
            print(f'GAME OVER! Você venceu {c} vezes')
            break
    elif escolha == 'I' and resultado == 0:
                print(f'{'=-'*50}')
                print(f'Você jogou {n} e o computador {nm}. Total de {n+nm} DEU PAR')
                print(f'{'=-'*50}')
                print(f'Você PERDEU!')
                print(f'GAME OVER! Você venceu {c} vezes.')
                break
