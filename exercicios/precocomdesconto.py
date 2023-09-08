# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
preço_produto = float(input('Digite o valor original do produto: '))
valor_descontado = preço_produto - 0.05
desconto_total = (valor_descontado * 0.95)
print('Valor novo do produto: R$ ', desconto_total)