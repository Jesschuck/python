# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_op, cateto_adj)
print('A hipotenusa vai medir: {:.3f}'.format(hipotenusa))