# Crie um programa que mostre quanto uma pessoa tem em sua carteira e quantos dólares ela pode comprar.
carteira_possui = float(input('Quantos reais você possuí na sua carteira? '))
valor_dolar = 4.79
t = float(carteira_possui) / valor_dolar
print(f'Você pode comprar: {t:.2f} $')