# Exercício 6:

num1 = input('Insira um número: ').replace(',', '.')
num1 = float(num1)
num2 = input('Insira um número: ').replace(',', '.')
num2 = float(num2)
num3 = input('Insira um número: ').replace(',', '.')
num3 = float(num3)

num1_eh_maior = num1 > num2 and num1 > num3
num2_eh_maior = num2 > num3

if num1_eh_maior:
  print('O maior número é',num1)
elif num2_eh_maior:
  print('O maior número é',num2)
else:
  print('O maior número é',num3)