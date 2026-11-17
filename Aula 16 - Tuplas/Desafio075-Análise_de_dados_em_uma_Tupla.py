numeros = (
    int(input('Digite um número: ')), 
    int(input('Digite outro número: ')), 
    int(input('Digite mais um número: ')), 
    int(input('Digite o último número: ')))
par = 0
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {1+numeros.index(3)}° posição')
else:
    print('Não foi digitado valor 3')
for n in numeros:
    if n%2 == 0:
        par += 1
if par == 0:
    print('Não foi digitado nenhum valor par!')
else:
    print(f'Os valores pares digitados foram ', end='')
    for n in numeros:
        if n%2 == 0:
            print(f'{n} ', end='')
