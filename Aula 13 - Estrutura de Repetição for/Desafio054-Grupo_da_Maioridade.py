from datetime import date

atual = date.today().year
ano = []
c1 = 0
c2 = 0

for c in range(1, 8):
    n = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    ano.append(n)
    idade = atual - n
    if idade >= 21:
        c1 += 1
    else:
        c2 += 1
    #print(ano[c-1])

print(f'Todos os anos digitados: {ano}')
print(f'Ao todo tivemos {c1} pessoas maiores de idade')
print(f'E também tivemos {c2} pessoas menores de idade')
