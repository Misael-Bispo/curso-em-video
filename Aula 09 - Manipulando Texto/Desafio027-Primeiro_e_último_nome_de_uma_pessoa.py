nome = str(input('Digite seu nome completo: ')).strip()

lista = nome.split()
unome = len(lista)-1

print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {lista[(unome)]}')
