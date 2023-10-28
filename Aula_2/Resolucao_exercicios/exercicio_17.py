# Exercício 17:

#Função que calcula a quantidade de latas e o valor
def calcular_latas(total_tinta, tamanho_lata, preco_lata):
  qtd_latas = 0
  while total_tinta > 0:
    qtd_latas += 1
    total_tinta -= tamanho_lata
  total = preco_lata * qtd_latas
  return qtd_latas, total

area_pintar = float(input('Insira a área a ser pintada: '))

#Constantes do código:
DILUICAO = 6 #Metros por litro
LATA_GRANDE = 18 #Litros
PRECO_LATA_GRANDE = 80
LATA_PEQUENA = 3.6 #Litros
PRECO_LATA_PEQUENA = 25

#Calcular o total de tinta misturada acrescido em 10%
tinta_diluida = area_pintar / DILUICAO
total_tinta = tinta_diluida + (tinta_diluida * 0.10)

qtd_lata_grande, total_lata_grande = calcular_latas(total_tinta, LATA_GRANDE, PRECO_LATA_GRANDE)
qtd_lata_pequena, total_lata_pequena = calcular_latas(total_tinta, LATA_PEQUENA, PRECO_LATA_PEQUENA)

print(f'''Latas grandes: {qtd_lata_grande}\t Valor R${total_lata_grande}
Latas pequenas: {qtd_lata_pequena}\t Valor R${total_lata_pequena}''')

qtd_grande = 0
qtd_pequena = 0

#Calcula a mistura de latas grandes e pequenas
while total_tinta > 0:
  if total_tinta > LATA_GRANDE:
    qtd_grande += 1
    total_tinta -= LATA_GRANDE
  else:
    qtd_pequena += 1
    total_tinta -= LATA_PEQUENA

total_grande = qtd_grande * PRECO_LATA_GRANDE
total_pequena = qtd_pequena * PRECO_LATA_PEQUENA
total = total_grande + total_pequena
#Se misturar latas grandes e pequenas for o melhor caso, exibe ao usuário 
if total < total_lata_grande:
  print(f'Melhor opção: \n{qtd_grande} latas grandes e {qtd_pequena} latas pequenas \nValor: R${total}')