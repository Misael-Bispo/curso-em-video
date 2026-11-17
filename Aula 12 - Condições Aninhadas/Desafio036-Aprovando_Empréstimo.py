valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salario? '))
anos = int(input('Em quantos anos pretende pagar? '))

parcela = valor / ( 12 * anos)
teto = sal * (30 / 100)

print(f'\nValor da Parcela é R${parcela:.2f} e valor minimo R${teto:.2f} \n')

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcela:.2f}')

if parcela <= teto:
    print('Emprestimo Aprovado!')
else:
    print('Emprestimo Negado!')
