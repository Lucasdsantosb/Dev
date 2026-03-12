"""
Faça um programa que leia um número e mostre na tela o seu
sucessor e seu antecessor
"""
n = int(input('Digite um número: ')) # Mensagem que solicita um número ao úsuario, e guarda a resposta na variavel: n1.

a = n - 1 # A significa antecessor
s = n + 1  # S significa sucessor

print(f'Você escolheu o número: {n}, que tem como o seu antecessor o número {a}, e tem o seu sucessor o número {s}') # Saída do resultado
