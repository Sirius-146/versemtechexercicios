# Exercício 4:

letra = input('Insira uma letra: ').lower()

vogais = ['a', 'e', 'i', 'o', 'u']

vogal = letra in vogais

if vogal:
  print('A letra informada é vogal')
else:
  print('A letra informada é consoante')