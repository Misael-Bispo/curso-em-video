lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #tuplas
lanches = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim'] #listas
lanches[2] = 'Picole' #listas podem ser modificadas
print(lanches[2])
lanches.append('Cockie')
lanches.insert(1,'Cachorro-Quente')
print(lanches)
del lanches[3]
lanches.pop()
if 'Hambúrguer' in lanches:
    lanches.remove('Hambúrguer')
print(lanches)
valores = list(range(4,11))
print(f'{valores}')
embaralhado = [8,2,5,4,9,3,0]
embaralhado.sort()
embaralhado.sort(reverse=True)
print(f'{embaralhado}')