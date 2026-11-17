print(f'{'-'*50}')
print(f'{'LOJA SUPER BARATÃO':^50}')
print(f'{'-'*50}')
tot = p1000 = c = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    c += 1
    if c == 1 or preço < mpreço:
         mproduto = produto
         mpreço = preço
    tot += preço
    if preço > 1000:
         p1000 += 1
    escolha = ' '
    while escolha not in 'SN':
          escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
         break
print(f'{'FIM DO PROGRAMA':-^50}')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {p1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {mproduto} que custa R${mpreço:.2f}')
