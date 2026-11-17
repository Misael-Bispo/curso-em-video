nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

total = len(nome)
espaço = nome.count(' ')
letras = total - espaço

print(f'Seu nome tem ao todo {letras} letras')

pnome = nome.split()
print(f'Seu primeiro nome é {pnome[0]} e ele tem {len(pnome[0])} letras')
