matriz = [[], [], []]

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('-=' * 30)
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')