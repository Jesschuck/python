# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente de um ângulo.
import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {:.0f} tem o seno de: {:.3f}'.format(angulo, seno))
print('O ângulo de {:.0f} tem o cosseno de: {:.3f}'.format(angulo, cosseno))
print('O ângulo de {:.0f} tem o tangente de: {:.3f}'.format(angulo, tangente))