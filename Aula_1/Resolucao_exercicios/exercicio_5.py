# Exercício 5:

valor_str = float(input("Insira o valor total da conta: ")) #Recebe o valor da conta
valor_str = valor_str.replace(',', '.') #Trata erros de digitação
valor = float(valor_str) #Transforma em float

gorjeta_str = input("Insira a porcentagem de gorjeta que deseja dar: ") #Recebe a porcentagem da gorjeta
gorjeta_str = gorjeta_str.replace(',', '.') #Trata erros de digitação
gorjeta = float(gorjeta_str) #Transforma em float

novo_total = valor + (valor * (gorjeta / 100)) #Faz o cálculo do novo valor com acréscimo de gorjeta
print(f'Com esse valor de gorjeta o total agora é: R${novo_total:.2f}') #Exibe o novo valor formatado