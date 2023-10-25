# Exercício 3:

sex = input('Insira seu gênero:(M/F) ').upper()

masc = sex == 'M'
fem = sex == 'F'

if masc:
  print('M - Masculino')
elif fem:
  print('F - Feminino')
else:
  print('Sexo Inválido')