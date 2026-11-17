from math import sin, cos, tan, radians
angulo_graus = float(input('Digite o valor do ângulo: '))
angulo_radianos = radians(angulo_graus)
print(f'O ângulo {angulo_graus} tem SENO de {sin(angulo_radianos):.2f}')
print(f'O ângulo {angulo_graus} tem COSSENO de {cos(angulo_radianos):.2f}')
print(f'O ângulo {angulo_graus} tem TANGENTE de {tan(angulo_radianos):.2f}')
