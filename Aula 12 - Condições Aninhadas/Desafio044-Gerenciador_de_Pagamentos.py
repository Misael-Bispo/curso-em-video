valor = float(input('Preço das compras: R$'))
e = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Sua opção: '''))

if e == 1:
    n = valor - (valor * 10 / 100)
elif e == 2:
    n = valor - (valor * 5 / 100)
elif e == 3:
    n = valor
    pag = n / 2
    print(f'Sua compra será parcelada em 2x de R${pag:.2f} SEM JUROS')
elif e == 4:
    parcelas = int(input('Quantas parcelas? '))
    n = valor + (valor * 20 / 100)
    pag = n / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${pag:.2f} COM JUROS')
else:
    n = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print(f'Sua compra de R${valor:.2f} vai custar R${n:.2f} no final.')
