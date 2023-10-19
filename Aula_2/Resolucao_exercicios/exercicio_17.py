# Exercício 17:

area_pintar = float(input('Insira a área a ser pintada: ')) #Recebe o valor da área de pintura

l_por_m = area_pintar / 6 #Calcula a quantidade de litros por metro
lata_grande = 18 #Tamanho da lata
preco_lata_grande = 80 #Preço da lata
lata_pequena = 3.6 #Tamanho da lata
preco_lata_pequena = 25 #Preço da lata

#O valor é acrescido em 1 para mantê-lo inteiro, visto que não é possível comprar 3/4 de lata, por exemplo
qtd_de_lata = l_por_m // lata_grande + 1 #Calcula a quantidade de latas
total_lata_grande = preco_lata_grande * qtd_de_lata #Calcula o valor final

#O valor é acrescido em 1 para mantê-lo inteiro, visto que não é possível comprar 3/4 de lata, por exemplo
qtd_de_latas = l_por_m // lata_pequena + 1 #Calcula a quantidade de latas
total_lata_pequena = preco_lata_pequena * qtd_de_latas #Calcula o valor final

#Exibe ao usuário a quantidade de latas grandes ou pequenas e o valor final a ser pago em cada escolha
print(f'''Quantidade de latas grandes: {int(qtd_de_lata)} \nValor a pagar R${total_lata_grande}
Quantidade de latas pequenas: {int(qtd_de_latas)} \nValor a pagar R${total_lata_pequena}''')

#Ainda há pontos a serem implementados, por exemplo a otimização de latas grandes e pequenas