# Exercício 5:

nota_1 = input('Insira sua nota: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
nota_1 = float(nota_1) #Transforma o valor recebido e reformatado em float
nota_2 = input('Insira sua nota: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
nota_2 = float(nota_2) #Transforma o valor recebido e reformatado em float

media = (nota_1 + nota_2) / 2 #Calcula a média

NOTA_MAXIMA = 10 #Define nota máxima
MEDIA_APROVACAO = 7 #Define o mínimo para aprovação

super_aprovado = media == NOTA_MAXIMA #Se a média é igual a nota máxima
aprovado = media >= MEDIA_APROVACAO #Se a média é suficiente para aprovação

if super_aprovado: #Testa se o retorno da variável é verdadeiro
  print('Aprovado com Distinção') #Imprime o valor na tela
elif aprovado: #Testa se o retorno da variável é verdadeiro
  print('Aprovado') #Imprime o valor na tela
else: #Caso o valor seja falso
  print('Reprovado') #Imprime o valor na tela