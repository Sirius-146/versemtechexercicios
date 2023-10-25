# Exercício 10:

print('Qual seu turno? \nM - matutino \nV - vespertino \nN - noturno')
turno = input().upper()

matutino = turno == 'M'
vespertino = turno == 'V'
noturno = turno == 'N'

if matutino:
  print('Bom Dia!')
elif vespertino:
  print('Boa Tarde!')
elif noturno:
  print('Boa Noite!')
else:
  print('Valor Inválido!')