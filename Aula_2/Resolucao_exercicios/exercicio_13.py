# Exercício 13:

altura_str = input('Insira sua altura: ') #Recebe o valor da altura
altura_str = altura_str.replace(',', '.') #Trata erros de digitação
altura = float(altura_str) #Transforma em float

#O peso ideal masculino é a altura multiplicada por 72.7, menos 52
peso_ideal_homem = (72.7*altura) - 58 #Calcula o peso ideal

#O peso ideal feminino é a altura multiplicada por 62.1, menos 44.7
peso_ideal_mulher = (62.1*altura) - 44.7 #Calcula o peso ideal

#Exibe o valor formatado ao usuário
print(f'Seu peso ideal é: \nCaso seja homem: {peso_ideal_homem:.2f}Kg \nCaso seja mulher: {peso_ideal_mulher:.2f}Kg')