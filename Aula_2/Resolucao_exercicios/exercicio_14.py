# Exercício 13:

peso_str = input("Peso dos peixes: ") #Recebe o valor
peso_str = peso_str.replace(',', '.') #Trata erros de digitação
peso = float(peso_str) #Transforma em float

LIMITE_PESO = 50 #Peso máximo permitido
VALOR_MULTA = 4 #Multa por excesso de peso

excesso = peso - LIMITE_PESO #Calcula se há excesso de peso
multa = excesso * VALOR_MULTA #Se houver, calcula o valor da multa

#Exibe ao usuário o peso de peixe, se foi superado o limite e, em caso afirmativo, o valor da multa
print(f'Peso inserido {peso}Kg.\nSuperando o limite em {excesso}Kg, gerando uma multa de R${multa}')

#Nesse caso, não há tratamento de erros para não existência de excesso
#Você pode testar implementá-lo utilizando o operador condicional