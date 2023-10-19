# Exercício 12:

altura_str = input('Insira sua altura: ') #Recebe o valor da altura
altura_str = altura_str.replace(',', '.') #Trata erros de digitação
altura = float(altura_str) #Transforma em float

#O peso ideal é a altura multiplicada por 72.7, menos 52
peso_ideal = (72.7*altura) - 58 #Calcula o peso ideal

print(f'Seu peso ideal é {peso_ideal:.2f}Kg') #Exibe o valor formatado ao usuário