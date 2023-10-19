# Exercício 4:

nota1_str = input('Insira sua nota: ') #Recebe o valor da nota
nota1_str = nota1_str.replace(',', '.') #Trata erros de digitação
nota1 = float(nota1_str) #Transforma em float

nota2_str = input('Insira sua nota: ') #Recebe o valor da nota
nota2_str = nota2_str.replace(',', '.') #Trata erros de digitação
nota2 = float(nota2_str) #Transforma em float

nota3_str = input('Insira sua nota: ') #Recebe o valor da nota
nota3_str = nota3_str.replace(',', '.') #Trata erros de digitação
nota3 = float(nota3_str) #Transforma em float

nota4_str = input('Insira sua nota: ') #Recebe o valor da nota
nota4_str = nota4_str.replace(',', '.') #Trata erros de digitação
nota4 = float(nota4_str) #Transforma em float

#Soma as notas e armazena o valor em uma nova variável
soma_das_notas = nota1 + nota2 + nota3 + nota4
TOTAL_NOTAS_INSERIDAS = 4 #Quantidade de notas inseridas

media = soma_das_notas / TOTAL_NOTAS_INSERIDAS

print(f'A média é {media}') #Imprime o valor da média para o usuário


#RESOLUÇÃO AVANÇADA
notas = [] #Cria uma lista para armazenar os valores
counter = 4 #Define o máximo de repetições

while counter > 0: #Valida o valor do contador
  nota = int(input('Insira sua nota: ')) #Pede um valor ao usuário
  notas.append(nota) #Adiciona o valor de nota à lista
  counter -= 1 #Decrementa o contador

#Usa a função sum() para somar as notas e divide pelo comprimento fornecido por len()
media = sum(notas) / len(notas) #Armazena o valor na variável média

print(f'A média é {media}') #Imprime o valor da média para o usuário