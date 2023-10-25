# Exercício 9:

n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
n3 = int(input('Insira um número: '))

n1_maior = n1 > n2 and n1 > n3
n2_maior = n2 > n1 and n2 > n3
n3_maior = n3 > n2 and n3 > n1

ordem1 = n3_maior and n2 > n1
ordem2 = n3_maior and n1 > n2
ordem3 = n1_maior and n2 > n3
ordem4 = n1_maior and n3 > n2
ordem5 = n2_maior and n3 > n1
ordem6 = n2_maior and n1 > n3

if ordem1:
  print(n3, n2, n1)
elif ordem2:
  print(n3, n1, n2)
elif ordem3:
  print(n1, n2, n3)
elif ordem4:
  print(n1, n3, n2)
elif ordem5:
  print(n2, n3, n1)
else:
  print(n2, n1, n3)