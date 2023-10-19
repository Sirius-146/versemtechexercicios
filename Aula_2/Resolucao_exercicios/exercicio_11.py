# Exercício 11:

numero1 = int(input('Insira um número inteiro: ')) #Recebe um valor e converte para inteiro
numero2 = int(input('Insira outro número inteiro: ')) #Recebe um valor e converte para inteiro

numero3_str = input('Insira um número real: ') #Recebe um valor
numero3_str = numero3_str.replace(',', '.') #Trata erros de digitação
numero3 = float(numero3_str) #Transforma em float

#Realiza as operações pedidas
a = (numero1 * 2) * (numero2 * 0.5) #Calcula o produto do dobro do primeiro com a metade do segundo
b = (numero1 * 3) + (numero3) #Calcula a soma do triplo do primeiro com o terceiro
c = numero3**3 #Calcula o cubo do terceiro

#Exibe os valores ao usuário
print(f'A) produto do dobro do primeiro e metade do segundo: {a} \nB) soma do triplo do primeiro com o terceiro: {b} \nC) terceiro elevado ao cubo: {c}')