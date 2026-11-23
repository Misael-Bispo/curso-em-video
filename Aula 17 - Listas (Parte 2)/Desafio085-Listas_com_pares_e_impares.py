temp = []
par = []
impar = []
princ = []

for c in range(7):
    temp.append(int(input(f'Digite o {c+1}º valor: ')))

for c in temp:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

par.sort()
impar.sort()
princ.append(par[:])
princ.append(impar[:])

print('-=' * 50)
print(f'Os dados foram {princ}')
print(f'Os valores pares digitados foram: {princ[0]}')
print(f'Os valores impares digitados foram {princ[1]}')