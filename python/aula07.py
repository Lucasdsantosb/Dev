n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))

s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #divisão inteira
p = n1 ** n2 #potenciação

print(f'A soma é {s}, O produto é {m} e a divisão é {d:.2f}')
print(f'Divisão inteira {di} e potência {p:.2f}')
