s = 0
v = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        v += 1
print(f'A soma de todos os {v} valores solicitados é {s}')
