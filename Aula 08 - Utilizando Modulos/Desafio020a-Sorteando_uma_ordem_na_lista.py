from random import shuffle

A1 = str(input('Primeiro aluno: '))
A2 = str(input('Segundo aluno: '))
A3 = str(input('Terceiro aluno: '))
A4 = str(input('Quarto aluno: '))

lista = [A1, A2, A3, A4]
print(f'O lista de alunos é {lista}')

shuffle(lista)

print(f'A ordem de apresentação é {lista}')
