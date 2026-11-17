print('-='*15)
print('Analisador de Triângulos')
print('-='*15)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    if n2 + n3 > n1:
        print('Forma triangulo')
    else:
        print('Não forma triangulo')

if n2 > n1 and n2 > n3:
    if n1 + n3 > n2:
        print('Não forma triangulo')
    else:
        print('Forma triangulo')

if n3 > n1 and n3 > n2:
    if n1 + n2 > n3:
        print('Forma triangulo')
    else:
        print('Não forma triangulo')
