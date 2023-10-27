# Exercício 3:

sex = input('Insira seu gênero:(M/F) ').upper() #Recebe um valor e transforma em maiúsculo

masc = sex == 'M' #Testa a igualdade do valor de sex
fem = sex == 'F' #Testa a igualdade do valor de sex

if masc: #Testa se o retorno de masc é verdadeiro
  print('M - Masculino') #Imprime o valor na tela
elif fem: #Testa se o retorno de fem é verdadeiro
  print('F - Feminino') #Imprime o valor na tela
else: #Caso o valor seja falso
  print('Sexo Inválido') #Imprime o valor na tela