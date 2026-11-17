print(f'{'':=^30}')
print(f'{'10 TERMOS DE UMA PA':^30}')
print(f'{'':=^30}')

p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

for c in range(p, (p + (10-1) * r) + 1, r):
    print(c, end=' → ')
print('FIM')
