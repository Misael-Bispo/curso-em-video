from random import sample

A1 = str(input('Primeiro aluno: '))
A2 = str(input('Segundo aluno: '))
A3 = str(input('Terceiro aluno: '))
A4 = str(input('Quarto aluno: '))

lista = [A1, A2, A3, A4]
ordem = sample(lista, k=4)

print(f'O lista de alunos é {lista}')
print(f'A ordem de apresentação é {ordem}')
