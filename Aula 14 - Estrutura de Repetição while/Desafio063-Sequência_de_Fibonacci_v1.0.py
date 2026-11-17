print('='*35)
print(f'{'Sequência de Fibonacci':^35}')
print('='*35)
termos = int(input(f'{'Quantos termos você quer mostrar? ':^30}'))
print('-'*35)

c = 1
n1 = 0
n2 = 1

while c <= termos:
    print(f'{n1}', end=' → ')
    print(f'{n2}', end=' → ')
    n1 += n2
    n2 += n1
    c += 2

print('FIM')
print('-'*35)
