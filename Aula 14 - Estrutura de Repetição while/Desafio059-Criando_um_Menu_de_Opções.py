from time import sleep

sair = False
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while not sair:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    escolha = int(input('>>>>> Qual é a sua opção? '))

    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif escolha == 2:
        multi = n1 * n2
        print(f'O resiltado de {n1} x {n2} é {multi}')
    elif escolha == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
        else:
            print(f' Os valores {n1} e {n2} são iguais')
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print(f'Finalizando...')
        sair = True
    else:
        print(f'Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)

print(f'Fim do programa! Volte sempre')
