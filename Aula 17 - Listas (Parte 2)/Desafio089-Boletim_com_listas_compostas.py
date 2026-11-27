ficha = list()
temp = []
nota = []

while True:
    temp.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    temp.append(nota[:])
    média = (nota[0] + nota[1]) / 2
    temp.append(média)
    ficha.append(temp[:])
    temp.clear()
    nota.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if resp in 'Nn':
        break

print('-=' * 50)
print(f'A lista completa é {ficha}')
print()
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 50)

for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
print('-' * 50)

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        print(f'Digite um número de aluno válido!')
print('VOLTE SEMPRE!')