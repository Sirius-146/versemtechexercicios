# Exercício 10:

print('Qual seu turno? \nM - matutino \nV - vespertino \nN - noturno') #Imprime o valor na tela
turno = input().upper() #Recebe um valor e transforma em maiúsculo

matutino = turno == 'M' #Testa a igualdade do valor de turno
vespertino = turno == 'V' #Testa a igualdade do valor de turno
noturno = turno == 'N' #Testa a igualdade do valor de turno

if matutino: #Testa se o retorno da variável é verdadeiro
  print('Bom Dia!') #Imprime o valor na tela
elif vespertino: #Testa se o retorno da variável é verdadeiro
  print('Boa Tarde!') #Imprime o valor na tela
elif noturno: #Testa se o retorno da variável é verdadeiro
  print('Boa Noite!') #Imprime o valor na tela
else: #Caso o valor seja falso
  print('Valor Inválido!') #Imprime o valor na tela