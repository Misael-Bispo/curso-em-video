s = float(input('Digite o salário do funcionário: R$'))

if s <= 1250:
    print(f'O novo salário com 15% de aumento é: R${(s + (s * (15 / 100))):.2f}')
else:
    print(f'O novo salário com 10% de aumento é: R${(s + (s * (10 / 100))):.2f}')
