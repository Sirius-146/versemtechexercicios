# Exercício 7:

lado_str = input('Insira a medida do lado do quadrado: ') #Recebe o valor do lado do quadrado
lado_str = lado_str.replace(',', '.') #Trata erros de digitação
lado = float(lado_str) #Transforma em float

#Area = lado multiplicado por ele mesmo
AREA = lado**2 #Calcula a área

print(AREA * 2) #Exibe ao usuário o valor do dobro da área 