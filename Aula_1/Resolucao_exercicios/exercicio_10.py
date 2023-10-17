# Exercício 10:

x1 = int(input('Insira a coordenada x1: ')) #Recebe o valor x da coordenada 1
y1 = int(input('Insira a coordenada y1: ')) #Recebe o valor y da coordenada 1
x2 = int(input('Insira a coordenada x2: ')) #Recebe o valor x da coordenada 2
y2 = int(input('Insira a coordenada y2: ')) #Recebe o valor y da coordenada 2

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #Realiza o cálculo da distância utilizando o Teorema de Pitágoras

print(f'A distância entre os pontos é: {distancia}') #Exibe a distância, que equivale a hipotenusa