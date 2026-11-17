print(f'{'':=^30}')
print(f'{'10 TERMOS DE UMA PA':^30}')
print(f'{'':=^30}')

p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = p
c = 1

while c <= 10:
    print(termo, end=' → ')
    termo += r
    c += 1
print('FIM')
