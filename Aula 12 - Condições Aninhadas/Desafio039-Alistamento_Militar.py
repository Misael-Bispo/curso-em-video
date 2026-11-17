an = int(input('Digite o seu ano de Nascimento: '))
aa = 2026

idade = aa - an
print(f'Quem nasceu em {an} tem {idade} em {aa}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    alistamento = idade - 18
    ano = aa - alistamento
    print(f'Você já deveria ter se alistado há {alistamento}')
    print(f'Seu alistamento será em {ano}')
else:
    alistamento = 18 - idade
    ano = aa + alistamento
    print(f'Ainda faltam {alistamento} anos para o alistamento')
    print(f'Seu alistamento será em {ano}')
