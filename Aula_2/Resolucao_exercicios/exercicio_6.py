# Exercício 6:

raio_str = input('Insira o raio do círculo: ') #Recebe o valor do raio
raio_str = raio_str.replace(',', '.') #Trata erros de digitação
raio = float(raio_str) #Transforma em float

PI = 3.1416 #Guarda o valor do Pi como constante

#Área = pi multiplicado pelo quadrado do raio
area = PI * raio**2 #Calcula a área

print(f'A área desse círculo é: {area}') #Retorna o valor da área ao usuário