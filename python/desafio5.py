"""
Faça um programa que leia um número e mostre na tela o seu
sucessor e seu antecessor
"""
n1 = int(input('Digite um número: ')) # Mensagem que solicita um número ao úsuario, e guarda a resposta na variavel: n1.
s = n1 + 1  # S significa sucessor
a = n1 - 1 # A significa antecessor
print('Você escolheu o número: {}, que tem como o seu antecessor o número {}, e tem o seu sucessor o número {}'.format(n1,a,s)) # Saída do resultado
