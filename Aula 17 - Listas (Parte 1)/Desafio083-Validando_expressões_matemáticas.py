exp = str(input('Digite a expressão: '))
p1 = p2 = 0

for i, v in enumerate(exp):
    if v == '(':
        p1 += 1
    elif v == ')':
        p2 += 1

if p1 == p2:
    print('Sua expressão é válida!' )
else:
    print('Sua expressão está errada!' )
