alunos = list()
temp = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    média = (temp[1] + temp[2]) / 2
    temp.append(média)
    alunos.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if resp in 'Nn':
        break

print('-=' * 50)
print(f'A lista completa é {alunos}')
print()
print(f'No.     Nome    Média')
print('-' * 50)

for i, l in enumerate(alunos):
    print(f'{i+1}       {l[0]}      {l[3]}')
print('-' * 50)