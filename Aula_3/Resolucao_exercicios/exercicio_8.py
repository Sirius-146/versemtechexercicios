# Exercício 8:

preco1 = input('Insira o preço do produto 1: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
preco1 = float(preco1) #Transforma o valor recebido e reformatado em float
preco2 = input('Insira o preço do produto 2: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
preco2 = float(preco2) #Transforma o valor recebido e reformatado em float
preco3 = input('Insira o preço do produto 3: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
preco3 = float(preco3) #Transforma o valor recebido e reformatado em float

menor_preco1 = preco1 < preco2 and preco1 < preco3 #Testa se o primeiro preço é menor que os demais
menor_preco2 = preco2 < preco3 #Testa se o segundo preço é maior que o terceiro

if menor_preco1: #Testa se o retorno da variável é verdadeiro
  print('Compre o produto 1!') #Imprime o valor na tela
elif menor_preco2: #Testa se o retorno da variável é verdadeiro
  print('Compre o produto 2!') #Imprime o valor na tela
else: #Caso o valor seja falso
  print('Compre o produto 3!') #Imprime o valor na tela