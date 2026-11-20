print('-' * 50)
print(f'{"Extraindo Valores":^50}')
print('-' * 50)

listanum = []
while True:
    while True:
        try:
            n = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Valor inválido! Digite um número inteiro.')

    listanum.append(n)

    escolha = ''
    while escolha not in ('S', 'N'):
        escolha = input('Quer continuar? [S/N] ').strip().upper()[:1]
    if escolha == 'N':
        break

print('-' * 50)
listanum.sort()
print(f'Os valores em ordem crescente são {listanum}')
print(f'Você digitou {len(listanum)} elementos.')
listanum.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listanum}')
if 5 in listanum:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
