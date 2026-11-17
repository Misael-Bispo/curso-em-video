frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

'''print(f'Você digitou a frase {junto}')
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    #print(junto[letra], end='')
    inverso += junto[letra]'''

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
