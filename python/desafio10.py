"""
Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
Considere 1$ = R$3,27
"""
carteira = float(input('Quanto Você tem na sua carteira? '))
cotacao = 3.27
dolar = carteira / cotacao
print ('Você tem um saldo de {}, então você consegue comprar: {:.2f} dólares.' .format(carteira,dolar))
