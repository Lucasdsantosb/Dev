"""
Desenvolva um programa que leia as duas notas de um aluno, calcule
e mostre a sua média
"""
n1 = float(input('Digite a sua nota do primeiro semestre: ')) #Solicita dados para o usuario
n2 = float(input('Digite a sua nota do segundo semestre: ')) #Solicita dados para o usuario

media = (n1 + n2) / 2 #operações internas

print (f'A sua média final é {media:.2f}') #Resultado final
