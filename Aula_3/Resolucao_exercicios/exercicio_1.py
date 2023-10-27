# Exercício 1:

num1 = int(input('Insira um número: ')) #Recebe o primeiro número
num2 = int(input('Insira um número: ')) #Recebe o segundo número

maior = num1 > num2 #Compara os valores

if maior: #Testa se o retorno é verdadeiro
  print(f'O maior é {num1}') #Imprime o valor na tela
else: #Caso o valor seja falso
  print(f'O maior é {num2}') #Imprime o valor na tela