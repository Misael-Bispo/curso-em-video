totH = totM20 = tot18 = 0 
while True:
    print(f'{'-'*50}')
    print(f'{'CADASTRE UMA PESSOA':^50}')
    print(f'{'-'*50}')
    idade = ' '
    while True:
        try: idade = int(input('Idade: ')); break
        except ValueError: pass
    sexo = ' '
    while sexo not in 'MF':
          sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print(f'{'-'*50}')
    if idade >= 18:
         tot18 += 1
    if sexo == 'M':
         totH += 1
    if sexo == 'F' and idade < 20:
         totM20 += 1
    escolha = ' '
    while escolha not in 'SN':
          escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
         break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')