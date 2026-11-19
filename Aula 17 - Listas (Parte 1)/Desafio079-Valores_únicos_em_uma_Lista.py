print(f'{'-'*50}')
print(f'{'Valores Únicos':^50}')
print(f'{'-'*50}')
listanum = list()
n = 0
while True:
    while True:
        try: n = (int(input('Digite um valor: '))); break
        except ValueError: pass
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    escolha = ' '
    while escolha not in 'SN':
          escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
         break
print(f'{'-'*50}')
listanum.sort()
print(f'{listanum}')
