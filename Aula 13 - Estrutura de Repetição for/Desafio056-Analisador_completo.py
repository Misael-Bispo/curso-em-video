sidade = 0
vnome = ''
hidade = 0
cont = 0

for c in range(1, 5):
    print(f'{f"{c}ª PESSOA":-^20}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    sidade += idade
    if sexo == 'M':
        if idade > hidade:
            hidade = idade
            vnome = nome
    elif sexo == 'F':
        if idade < 20:
            cont += 1

print(f'A média de idade do grupo é de {sidade/4} anos')
print(f'O homem mais velho tem {hidade} anos e se chama {vnome}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')
