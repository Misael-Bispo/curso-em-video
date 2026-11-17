ano = int(input('Digite um ano: '))

if ano%100 == 0:
    if ano%400 == 0:
        print(f'bissexto')
    else:
        print(f'Não é bissexto') 
else:
    if ano%4 ==0:
        print(f'bissexto')
    else:
        print(f'Não é bissexto')
        