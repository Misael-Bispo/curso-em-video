p = (
    'Hambúrguer', 5, 
    'Pizza', 6.1)
print(f'{'-'*50}')
print(f'{'LISTAGEM DE PREÇOS':^50}')
print(f'{'-'*50}')
for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<40}', end='')
    else:
        print(f'R${p[pos]:7.2f}')
print(f'{'-'*50}')