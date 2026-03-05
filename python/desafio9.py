"""
Crie um programa que leia um numero inteiro qualquer,
e mostre na tela a sua tabuada
"""
num = int(input('Digite um número para visualizar a sua tabuada: '))
for i in range (1, 11):
    print (f'{num} * {i} = {num * i}')
    