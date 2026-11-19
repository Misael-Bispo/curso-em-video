print('-' * 50)
print(f'{"Valores Únicos":^50}')
print('-' * 50)

listanum = []
while True:
    while True:
        try:
            n = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Valor inválido! Digite um número inteiro.')

    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    escolha = ''
    while escolha not in ('S', 'N'):
        escolha = input('Quer continuar? [S/N] ').strip().upper()[:1]
    if escolha == 'N':
        break

print('-' * 50)
listanum.sort()
print(listanum)