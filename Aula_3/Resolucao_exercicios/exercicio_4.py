# Exercício 4:

letra = input('Insira uma letra: ').lower() #Recebe um valor e transforma em minúsculo

vogais = ['a', 'e', 'i', 'o', 'u'] #Cria uma lista com vogais

vogal = letra in vogais #Testa se a letra inserida está na lista

if vogal: #Testa se o retorno da variável é verdadeiro
  print('A letra informada é vogal') #Imprime o valor na tela
else: #Caso o valor seja falso
  print('A letra informada é consoante') #Imprime o valor na tela