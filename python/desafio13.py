"""
Faça um algoritmo que leia o salario de um funcionário a mostre
seu novo salario, com 15% de aumento.
"""
salario = float(input('Digite o seu salário para aplicar um aumento de 15%: '))
aumento = salario * 0.15
novo_salario = salario + aumento

print (f'Você teve um aumento de {aumento}, portanto seu novo salário será de: {novo_salario}.')
#mesma lógica do exercicio anterior...