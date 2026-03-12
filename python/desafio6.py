"""
Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
"""
n = int(input('Digite um número: '))

d = n * 2 #D significa Dobro
t = n * 3 #T significa Triplo
rq = n**0.5 #RQ significa raiz quadrada

print (f'Você escolheu o número {n}, o dobro de {n} é {d}, o triplo de {n} é {t}, e a Raiz quadrada de {n} é {rq:.2f}')
