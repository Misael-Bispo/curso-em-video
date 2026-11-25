matriz = [[], [], []]
somapar = c3soma = l2maior = 0

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    c3soma += matriz[l][2]

l2maior = max(matriz[1])

print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {c3soma}')
print(f'O maior valor da segunda coluna é {l2maior}')