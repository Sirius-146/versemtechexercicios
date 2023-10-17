# Exercício 11:

n1 = int(input('Insira nota 1: ')) #Recebe o valor da nota 1
p1 = int(input('Insira o peso da nota 1: ')) #Recebe o peso da nota 1
n2 = int(input('Insira nota 2: ')) #Recebe o valor da nota 3
p2 = int(input('Insira o peso da nota 2: ')) #Recebe o peso da nota 2
n3 = int(input('Insira nota 3: ')) #Recebe o valor da nota 3
p3 = int(input('Insira o peso da nota 3: ')) #Recebe o peso da nota 3

#Média ponderada é a soma dos produtos (nota x peso) dividido pela soma dos pesos
media_ponderada = ((n1 * p1)+(n2 * p2)+(n3 * p3)) / (p1 + p2 + p3) #Calcula a média ponderada

print(f'A média ponderada é: {media_ponderada}') #Exibe o valor da média ponderada