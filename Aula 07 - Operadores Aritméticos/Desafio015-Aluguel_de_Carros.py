dias = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de Km percorridos: '))
preço = (dias*60) + (km*0.15)
print(f'O preço a ser pago é de R${preço:.2f}')
