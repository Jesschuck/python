# Crie um programa que escreva a tabuada de um número
n1 = int(input('Digite um número: '))
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in range (11):
    resultado = n1 * numero
    print(f'{n1} * {numero} = {resultado}')