from datetime import date

sexo = int(input('Escolha seu sexo: \n[ 1 ] Masculino\n[ 2 ] feminino\nSua opção: '))

if sexo == 1:
    an = int(input('Digite o seu ano de Nascimento: '))
    aa = date.today().year

    idade = aa - an
    print(f'Quem nasceu em {an} tem {idade} em {aa}')

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        alistamento = idade - 18
        ano = aa - alistamento
        print(f'Você já deveria ter se alistado há {alistamento} anos')
        print(f'Seu alistamento será em {ano}')
    elif idade < 18:
        alistamento = 18 - idade
        ano = aa + alistamento
        print(f'Ainda faltam {alistamento} anos para o alistamento')
        print(f'Seu alistamento será em {ano}')

elif sexo == 2:
    print(f'Você não precisa realizar o alistamento obrigatório!')
else:
    print('OPÇÃO INVALIDA')