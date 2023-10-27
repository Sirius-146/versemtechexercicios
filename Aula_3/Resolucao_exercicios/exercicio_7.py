# Exercício 7:

numero_1 = input('Insira um número: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
numero_1 = float(numero_1) #Transforma o valor recebido e reformatado em float
numero_2 = input('Insira um número: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
numero_2 = float(numero_2) #Transforma o valor recebido e reformatado em float
numero_3 = input('Insira um número: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
numero_3 = float(numero_3) #Transforma o valor recebido e reformatado em float

maior_eh_1 = numero_1 > numero_2 and numero_1 > numero_3 #Testa se o primeiro número é maior que os demais
maior_eh_2 = numero_2 > numero_3 #Testa se o segundo número é maior que o terceiro

if maior_eh_1: #Testa se o retorno da variável é verdadeiro
  print(f'O maior número é {numero_1}.') #Imprime o valor na tela
elif maior_eh_2: #Testa se o retorno da variável é verdadeiro
  print(f'O maior número é {numero_2}.') #Imprime o valor na tela
else: #Caso o valor seja falso
  print(f'O maior número é {numero_3}.') #Imprime o valor na tela

menor_eh_1 = numero_1 < numero_2 and numero_1 < numero_3 #Testa se o primeiro número é menor que os demais
menor_eh_2 = numero_2 < numero_3 #Testa se o segundo número é menor que o terceiro

if menor_eh_1: #Testa se o retorno da variável é verdadeiro
  print(f'O menor número é {numero_1}.') #Imprime o valor na tela
elif menor_eh_2: #Testa se o retorno da variável é verdadeiro
  print(f'O menor número é {numero_2}.') #Imprime o valor na tela
else: #Caso o valor seja falso
  print(f'O menor número é {numero_3}.') #Imprime o valor na tela

#RESOLUÇÃO AVANÇADA

numeros = []
counter = 3

while counter > 0:
  num = input('Insira um número: ').replace(',','.')
  NUM = float(num)
  numeros.append(num)
  counter -=1

print(f'O maior número é {max(numeros)}. \nO menor número é {min(numeros)}') #Imprime o valor na tela
