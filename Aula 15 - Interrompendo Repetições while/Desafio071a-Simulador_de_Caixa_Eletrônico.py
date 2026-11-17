print(f'{'-'*50}')
print(f'{'BANCO CEV':^50}')
print(f'{'-'*50}')
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
c50 = c20 = c10 = c1 =0

if total >= 50:
    c50 = total // 50
    total = total - c50 * 50
    print(f'Total de {c50} cédulas de R$50')

if total >= 20:
    c20 = total // 20
    total = total - c20 * 20
    print(f'Total de {c20} cédulas de R$20')

if total >= 10:
    c10 = total // 10
    total = total - c10 * 10
    print(f'Total de {c10} cédulas de R$10')

if total >= 1:
    c1 = total // 1
    total = total - c1 * 1
    print(f'Total de {c1} cédulas de R$1')

print(f'{'-'*50}')
print(f'{'Volte sempre ao BANCO CEV! Tenha um bom dia!':^50}')
