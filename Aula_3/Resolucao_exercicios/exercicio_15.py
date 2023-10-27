# Exercício 15:

#Recebe o valor da medida de cada lado
lado1 = int(input('Insira o valor dos lado: '))
lado2 = int(input('Insira o valor dos lado: '))
lado3 = int(input('Insira o valor dos lado: '))

#Testa se se encaixa nas regras para ser um triângulo válido
#Soma de 2 lados maior que o terceiro
triangulo_valido = (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado3 + lado2) > lado1

#Testa se pode ser um triângulo equilátero - Possuir três lados iguais
equilatero = lado1 == lado2 and lado2 == lado3 and lado3 == lado1
#Testa se pode ser um triângulo isósceles - Possuir dois lados iguais
isosceles = lado1 == lado2 or lado2 == lado3 or lado3 == lado1

if triangulo_valido: #Testa se é um triângulo válido
  print("Esse triângulo é válido")
  if equilatero: #Testa se o retorno da variável é verdadeiro
    print('Esse é um triângulo equilátero!')
  elif isosceles: #Testa se o retorno da variável é verdadeiro
    print('Esse é um triângulo isósceles!')
  else: #Caso o valor seja falso
    print('Esse é um triângulo escaleno!')
else: #Caso o valor seja falso. Não é triângulo
  print("Esse triângulo não é válido")