# Exercício 9:

n1 = int(input('Insira um número: ')) #Recebe um valor numérico
n2 = int(input('Insira um número: ')) #Recebe um valor numérico
n3 = int(input('Insira um número: ')) #Recebe um valor numérico

n1_maior = n1 > n2 and n1 > n3 #Testa se o primeiro número é maior que os demais
n2_maior = n2 > n1 and n2 > n3 #Testa se o primeiro número é maior que os demais
n3_maior = n3 > n2 and n3 > n1 #Testa se o primeiro número é maior que os demais

ordem1 = n3_maior and n2 > n1 #Testa se ambas comparações são verdadeiras
ordem2 = n3_maior and n1 > n2 #Testa se ambas comparações são verdadeiras
ordem3 = n1_maior and n2 > n3 #Testa se ambas comparações são verdadeiras
ordem4 = n1_maior and n3 > n2 #Testa se ambas comparações são verdadeiras
ordem5 = n2_maior and n3 > n1 #Testa se ambas comparações são verdadeiras
ordem6 = n2_maior and n1 > n3 #Testa se ambas comparações são verdadeiras

if ordem1: #Testa se o retorno da variável é verdadeiro
  print(n3, n2, n1) #Imprime os valores na tela
elif ordem2: #Testa se o retorno da variável é verdadeiro
  print(n3, n1, n2) #Imprime os valores na tela
elif ordem3: #Testa se o retorno da variável é verdadeiro
  print(n1, n2, n3) #Imprime os valores na tela
elif ordem4: #Testa se o retorno da variável é verdadeiro
  print(n1, n3, n2) #Imprime os valores na tela
elif ordem5: #Testa se o retorno da variável é verdadeiro
  print(n2, n3, n1) #Imprime os valores na tela
else: #Caso o valor seja falso
  print(n2, n1, n3) #Imprime os valores na tela