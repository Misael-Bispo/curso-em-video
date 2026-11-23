lista = list()
dado = list()
pesadas = list()
leves = list()
maior = menor = par = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if resp in 'Nn':
        break

maior = menor = lista[1]
for c in range (len(lista)):
    if c % 2 == 0:
        par += 1
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

for p in range (len(lista)):
    if c % 2 == 0:
        par += 1
    else:
        if lista[p] == maior:
            dado.append(lista[p-1])
            pesadas.append(dado[:])
            dado.clear()
        if lista[p] == menor:
            dado.append(lista[p-1])
            leves.append(dado[:])
            dado.clear()

print('-=' * 50)
print(f'A lista completa é {lista}')
print(f'Ao todo, você cadastrou {len(lista)/2:.0f} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {pesadas}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {leves}')
