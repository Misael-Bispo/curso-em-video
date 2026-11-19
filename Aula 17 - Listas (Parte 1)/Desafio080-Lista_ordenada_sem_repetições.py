valores = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if not valores or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while n > valores[pos]:
            pos += 1
        valores.insert(pos, n)
        print(f'Adicionado na posição {pos} da lista...')
print('-' * 50)
print(f'Os valores digitados em ordem foram {valores}')