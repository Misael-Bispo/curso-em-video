print('='*40)
print(f'{'Soma dos n Primeiros Números Ímpares e Pares':^40}')
print('='*40)

n = int(input(f'Quantos termos você quer mostrar? '))
somap = n * (n + 1)
somai = n ** 2

print(f'A soma dos {n} primeiros números pares é {somap} e dos números ímpares é {somai}')