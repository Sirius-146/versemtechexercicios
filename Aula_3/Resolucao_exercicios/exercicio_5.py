# Exercício 5:

nota_1 = input('Insira sua nota: ').replace(',', '.')
nota_1 = float(nota_1)
nota_2 = input('Insira sua nota: ').replace(',', '.')
nota_2 = float(nota_2)

media = (nota_1 + nota_2) / 2

NOTA_MAXIMA = 10
MEDIA_APROVACAO = 7

super_aprovado = media == NOTA_MAXIMA
aprovado = media >= MEDIA_APROVACAO

if super_aprovado:
  print('Aprovado com Distinção')
elif aprovado:
  print('Aprovado')
else:
  print('Reprovado')