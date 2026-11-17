n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {m}')

if m >= 7:
    print('O aluno está APROVADO.')
elif m < 7 and m >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')
