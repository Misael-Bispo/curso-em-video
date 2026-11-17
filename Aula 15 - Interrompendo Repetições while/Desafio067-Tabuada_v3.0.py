n = c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(f'{'='*50}')
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {c*n}')
    print(f'{'='*50}')
print('Programa Tabuada Encerado.')