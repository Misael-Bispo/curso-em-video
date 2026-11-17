pmaior = 0
pmenor = 0

for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}ª pessoa: '))

    if peso >= pmaior:
        pmaior = peso

    if peso < pmenor or pmenor == 0:
        pmenor = peso

print(f'O maior peso lido foi de {pmaior} Kg')
print(f'O menor peso lido foi de {pmenor} Kg')
