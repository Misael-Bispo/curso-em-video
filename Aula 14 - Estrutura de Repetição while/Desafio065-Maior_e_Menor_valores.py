escolha = False
cont = soma = 0

while escolha is False:
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'nN':
        escolha = True
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    cont += 1

média = soma / cont
print(f'Você digitou {cont} números e a média foi {média}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
