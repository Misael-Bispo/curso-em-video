dist = int(input('Qual a distância da viagem: '))
print(f'Você está prestes a começar uma viagem de {dist:.2f}Km.')
preço = dist*0.50 if dist <= 200 else dist*0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')
