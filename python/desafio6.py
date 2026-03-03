"""
Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
"""
n1 = int(input('Digite um número: '))
d = n1 * 2 #D significa Dobro
t = n1 * 3 #T significa Triplo
rq = n1** 0.5 #RQ significa raiz quadrada
print ('Você escolheu o número {}, o dobro de {} é {}, o triplo de {} é {}, e a Raiz quadrada de {} é {:.2f}'.format(n1,n1,d,n1,t,n1,rq))
