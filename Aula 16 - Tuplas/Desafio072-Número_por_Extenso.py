n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = ' '
while escolha not in range(0,21):
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha in range(0,21):
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {n[escolha]}')
