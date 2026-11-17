print('='*40)
print(f'{'Soma dos n Primeiros Números Ímpares':^40}')
print('='*40)

n = int(input(f'Quantos termos você quer mostrar? '))
soma = 0

for cont in range(2, (2 * n) + 1, 2):
    print(f'{cont}', end=' → ')
    soma += cont 
print('FIM')
print(f'A soma dos {n} primeiros números pares é {soma}')
