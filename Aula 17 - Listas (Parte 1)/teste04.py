a = [2, 3, 4, 7]
b = a
c = a[:]
b[2] = 8
c[1] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')