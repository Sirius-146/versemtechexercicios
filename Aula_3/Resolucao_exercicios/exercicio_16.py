# Exercício 16:

#Cria um laço de repetição para testar se a equação é do segundo grau
no_valid = 1
while no_valid:
    a_valor = int(input('Insira o valor de A: '))
    no_valid = a_valor == 0
    if no_valid:
        print('Equação não é do segundo grau')

#Recebe os demais valores
b_valor = int(input('Insira o valor de B: '))
c_valor = int(input('Insira o valor de C: '))

#Calcula o valor de Delta
BHASKARA = b_valor**2 - (4 * a_valor * c_valor)
#Calcula as raízes de Delta e o valor final da euqção
raiz1 = (-(b_valor) + BHASKARA**0.5) / (2*a_valor)
raiz2 = (-(b_valor) - BHASKARA**0.5) / (2*a_valor)

#Se delta for menor que 0, não há raízes reais
no_raizes_reais = BHASKARA < 0
#Se delta for igual a 0, há uma raíz real
uma_raiz_real = BHASKARA == 0

if no_raizes_reais: #Testa se o retorno da variável é verdadeiro
  print('A expressão não possui raízes reais')
elif uma_raiz_real: #Testa se o retorno da variável é verdadeiro
  print(f'A expressão possui uma raíz real: {raiz1}')
else:
  print(f'Os valores das raízes são: {int(raiz1)} e {int(raiz2)}')