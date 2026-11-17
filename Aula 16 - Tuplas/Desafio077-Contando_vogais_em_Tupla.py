p = (
    'aprender',
    'programar',
    'linguagem',
    'python'
)
for pos in range(0, len(p)):
    t = p[pos]
    print(f'Na palavra {p[pos]} temos ', end='')
    for pos2 in range(0, len(t)):
        if t[pos2] in 'aeiou':
            print(f' {t[pos2]}',end='')
    print('')
print(f'{'-'*50}')