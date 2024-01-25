# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import floor
num = float(input('Escreva um número qualquer quebrado: '))
inteiro = floor(num)
print('O valor inteiro do {} é {}'.format(num, inteiro))
