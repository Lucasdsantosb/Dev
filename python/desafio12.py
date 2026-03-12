"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""
preco = float(input('Para aplicar o desconto de 5% digite o preço do produto: '))
desconto = preco * 0.05
novo_preco = preco - desconto

print (f'O novo preço do produto é de: {novo_preco}')
