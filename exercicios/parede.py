# Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área
# de 2m quadrados
n1 = int(input('Digite a altura da parede: '))
n2 = int(input('Digite a largura da parede: '))
total = n1 * n2
litro = 2
tinta = total / litro
print(tinta)