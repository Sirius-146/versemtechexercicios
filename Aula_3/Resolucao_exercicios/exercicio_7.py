# Exercício 7:

numero_1 = input('Insira um número: ').replace(',','.')
numero_1 = float(numero_1)
numero_2 = input('Insira um número: ').replace(',','.')
numero_2 = float(numero_2)
numero_3 = input('Insira um número: ').replace(',','.')
numero_3 = float(numero_3)

maior_eh_1 = numero_1 > numero_2 and numero_1 > numero_3
maior_eh_2 = numero_2 > numero_3

if maior_eh_1:
  print(f'O maior número é {numero_1}.')
elif maior_eh_2:
  print(f'O maior número é {numero_2}.')
else:
  print(f'O maior número é {numero_3}.')

menor_eh_1 = numero_1 < numero_2 and numero_1 < numero_3
menor_eh_2 = numero_2 < numero_3

if menor_eh_1:
  print(f'O menor número é {numero_1}.')
elif menor_eh_2:
  print(f'O menor número é {numero_2}.')
else:
  print(f'O menor número é {numero_3}.')

#RESOLUÇÃO AVANÇADA

numeros = []
counter = 3

while counter > 0:
  num = input('Insira um número: ').replace(',','.')
  NUM = float(num)
  numeros.append(num)
  counter -=1

print(f'O maior número é {max(numeros)}. \nO menor número é {min(numeros)}')
