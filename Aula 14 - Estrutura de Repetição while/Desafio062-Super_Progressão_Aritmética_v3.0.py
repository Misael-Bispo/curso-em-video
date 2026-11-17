print(f'{'':=^30}')
print(f'{'TERMOS DE UMA PA':^30}')
print(f'{'':=^30}')

p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = p
c = 1
mais = 10
cont = mais

while mais != 0:
    while c <= mais:
        print(termo, end=' → ')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    cont += mais
    c = 1

print(f'Progressão finalizada com {cont} termos mostrados.')
