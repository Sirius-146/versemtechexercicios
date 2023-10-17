# Exercício 9:

preco_original_str = input('Digite o valor original: ') #Recebe o valor original do produto
preco_original_str = preco_original_str.replace(',', '.') #Trata erros de digitação
preco_original = float(preco_original_str) #Transforma em float

desconto = float(input('Digite a porcentagem de desconto: ')) #Recebe a porcentagem de desconto
novo_preco = preco_original - preco_original * (desconto / 100) #Calcula o novo preço

print(f'De: R${preco_original:.2f} \nPor: R${novo_preco:.2f}') #Exibe o valor original e o novo valor