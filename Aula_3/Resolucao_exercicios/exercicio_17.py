# Exercício 17:

#Recebe o valor do ano
year = int(input('Insira o ano: '))

#REGRAS PARA SER BISSEXTO
#Ano ser múltiplo de 4 e não ser múltiplo por 100
RULE1 = year % 4 == 0 and year % 100 != 0
#Se for múltiplo de 100, tem que ser de 400 também
RULE2 = year % 400 == 0

#Obedece a uma das regras anteriores
eh_bissexto = RULE1 or RULE2

if eh_bissexto: #Testa se o retorno da variável é verdadeiro
  print(f'O ano {year} é bissexto')
else: #Caso seja falso
  print(f'O ano {year} não é bissexto')