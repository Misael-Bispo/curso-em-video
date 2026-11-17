n = int(input('Digite um número: '))
cont = 0

for c in range (1, n+1):
    print(c, end=' ')
    if n % c == 0:
        cont += 1

if cont == 2:
    print(f'\nO número {n} foi divisível {cont} vezes')
    print(f'E por isso ele É PRIMO!')
else:
    print(f'\nO número {n} foi divisível {cont} vezes')
    print(f'E por isso ele NÃO É PRIMO!')
