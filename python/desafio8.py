"""
Crie um programa que leia um valor em metros e o exiba convertido
em centimetros e milimetros
"""
M = float(input('Digite o valor em metros: '))
C = M * 100
MM = C * 10 
print ('O tamanho selecionado convertido para centimetros é: {}'.format(C))
print ('Em milimetros é: {}'.format(MM))
