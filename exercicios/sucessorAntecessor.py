# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor do número
antecessor = numero - 1
sucessor = numero + 1

# Exibe os resultados na tela
print(f"O antecessor de {numero} é {antecessor}.")
print(f"O sucessor de {numero} é {sucessor}.")
