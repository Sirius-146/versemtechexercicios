# Exercício 8:

preco1 = input('Insira o preço do produto 1: ').replace(',','.')
preco1 = float(preco1)
preco2 = input('Insira o preço do produto 2: ').replace(',','.')
preco2 = float(preco2)
preco3 = input('Insira o preço do produto 3: ').replace(',','.')
preco3 = float(preco3)

menor_preco1 = preco1 < preco2 and preco1 < preco3
menor_preco2 = preco2 < preco3

if menor_preco1:
  print('Compre o produto 1!')
elif menor_preco2:
  print('Compre o produto 2!')
else:
  print('Compre o produto 3!')