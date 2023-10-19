# Exercício 5:

metro_str = input('Insira o valor em metros: ') #Recebe o valor em metros
metro_str = metro_str.replace(',', '.') #Trata erros de digitação
metro = float(metro_str) #Transforma em float

CM_POR_M = 100 #Quantidade de centímetros em um metro
centimetro = metro * CM_POR_M #Calcula os centímetros na quantidade de metros inseridos

print(f'O valor em centímetros é {int(centimetro)}') #Retorna o valor ao usuário