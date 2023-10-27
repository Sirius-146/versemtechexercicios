# Exercício 14:

nota1 = input('Insira sua nota: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
nota1 = float(nota1) #Transforma o valor recebido e reformatado em float
nota2 = input('Insira sua nota: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
nota2 = float(nota2) #Transforma o valor recebido e reformatado em float

AVG = (nota1 + nota2) / 2 #Calcula a média

nota_A = AVG >= 9 #A nota será A se a média for maior igual a 9
nota_B = AVG >= 7.5 #A nota será B se a média for maior igual a 7.5
nota_C = AVG >= 6 #A nota será C se a média for maior igual a 6
nota_D = AVG >= 4 #A nota será D se a média for maior igual a 9

#Imprime o valor na tela
print(f'Nota 1: {nota1} \nNota 2: {nota2} \nMédia: {AVG}')

if nota_A: #Testa se o retorno da variável é verdadeiro
  print('Conceito: A \nAprovado!') #Imprime o valor na tela
elif nota_B: #Testa se o retorno da variável é verdadeiro
  print('Conceito: B \nAprovado!') #Imprime o valor na tela
elif nota_C: #Testa se o retorno da variável é verdadeiro
  print('Conceito: C \nAprovado!') #Imprime o valor na tela
elif nota_D: #Testa se o retorno da variável é verdadeiro
  print('Conceito: D \nReprovado!') #Imprime o valor na tela
else: #Caso o valor seja falso
  print('Conceito: E \nReprovado!') #Imprime o valor na tela