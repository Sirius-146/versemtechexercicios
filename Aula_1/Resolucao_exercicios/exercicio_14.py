# Exercício 14:

altura_str = input("Insira sua altura em metros: ") #Recebe o valor da altura em metros
altura_str = altura_str.replace(',', '.') #Trata erros de digitação
altura = float(altura_str) #Transforma em float

peso_str = input("Insira seu peso em quilogramas: ") #Recebe o peso em Kg
peso_str = peso_str.replace(',', '.') #Trata erros de digitação
peso = float(peso_str) #Transforma em float

imc = peso / altura**2 #Calcula o IMC. Peso divido por altura ao quadrado

print(f'Seu índice de massa corpórea é {imc:.3f}') #Exibe o valor de IMC