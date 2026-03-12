"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².
"""
largura = float(input('Digite a Largura da parede: '))
altura = float(input('Digite a Altura da parede: '))
area = largura * altura
tinta = area / 2

print (f'A quantidade de litros necessário para pintar a parede é de: {tinta :.2f} litros')
