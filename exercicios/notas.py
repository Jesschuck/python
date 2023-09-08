# Desenvolva um programa que leia as duas notas de um aluno, calcule  mostre a sua média
n1 = int(input('Digite a sua primeira note: '))
n2 = int(input('Digite a sua segunda nota: '))
s = (n1 + n2) / 200
t = s * 100
print('A sua nota final é: {:.1f}'.format(t))