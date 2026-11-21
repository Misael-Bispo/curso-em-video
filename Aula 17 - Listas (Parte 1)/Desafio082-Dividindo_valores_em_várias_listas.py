print('-' * 50)
print(f'{"Dividindo Valores":^50}')
print('-' * 50)

listanum = []
numpar = []
numimpar = []

while True:
    while True:
        try:
            n = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Valor inválido! Digite um número inteiro.')

    listanum.append(n)
    
    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)

    escolha = ''
    while escolha not in ('S', 'N'):
        escolha = input('Quer continuar? [S/N] ').strip().upper()[:1]
    if escolha == 'N':
        break

print('-' * 50)
print(f'A lista completa é {listanum}')
print(f'A lista de pares é {numpar}')
print(f'A lista de ímpares é {numimpar}')
