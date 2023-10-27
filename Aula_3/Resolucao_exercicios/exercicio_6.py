# Exercício 6:

num1 = input('Insira um número: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
num1 = float(num1) #Transforma o valor recebido e reformatado em float
num2 = input('Insira um número: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
num2 = float(num2) #Transforma o valor recebido e reformatado em float
num3 = input('Insira um número: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
num3 = float(num3) #Transforma o valor recebido e reformatado em float

num1_eh_maior = num1 > num2 and num1 > num3 #Testa se o primeiro número é maior que os demais
num2_eh_maior = num2 > num3 #Testa se o segundo número é maior que o terceiro

if num1_eh_maior: #Testa se o retorno da variável é verdadeiro
  print('O maior número é',num1) #Imprime o valor na tela
elif num2_eh_maior: #Testa se o retorno da variável é verdadeiro
  print('O maior número é',num2) #Imprime o valor na tela
else: #Caso o valor seja falso
  print('O maior número é',num3) #Imprime o valor na tela