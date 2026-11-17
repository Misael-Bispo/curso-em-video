print('-='*15)
print('Analisador de Triângulos')
print('-='*15)

n1 = int(input('Digite o primeiro segmento: '))
n2 = int(input('Digite o segundo segmento: '))
n3 = int(input('Digite o terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 +n2:
    print('Os segmentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
