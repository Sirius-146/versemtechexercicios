# Exercício 16:

area_pintura = float(input('Insira a área a ser pintada: ')) #Recebe o valor da área de pintura

litro_por_metro = area_pintura / 3 #Calcula a quantidade de litros por metro
tamanho_lata = 18 #Tamanho da lata
valor_lata = 80 #Preço da lata

#O valor é acrescido em 1 para mantê-lo inteiro, visto que não é possível comprar 3/4 de lata, por exemplo
qtd_lata = litro_por_metro // tamanho_lata + 1 #Calcula a quantidade de latas
valor_total = valor_lata * qtd_lata #Calcula o valor final

#Exibe ao usuário a quantidade de latas e o valor final a ser pago
print(f'Quantidade de latas: {int(qtd_lata)} \nValor a pagar R${valor_total}')