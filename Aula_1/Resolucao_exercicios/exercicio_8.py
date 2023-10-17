# Exercício 8:

montante_str = input('Digite o montante inicial: ') #Recebe o valor do montante inicial
montante_str = montante_str.replace(',', '.') #Trata erros de digitação
montante = float(montante_str) #Transforma em float

taxa_juros_str = input('Digite a taxa de juros ao ano: ') #Recebe a taxa de juros
taxa_juros_str = taxa_juros_str.replace(',', '.') #Trata erros de digitação
taxa_juros = float(taxa_juros_str) #Transforma em float

anos = int(input('Digite o tempo (em anos): ')) #Recebe o tempo em anos

juros_simples = montante * (taxa_juros / 100) * anos #Calcula o rendimento

print(f'O valor pago em juros foi: R${juros_simples:.2f}') #Exibe o rendimento formatado