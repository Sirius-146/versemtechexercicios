# Exercício 6:

print('Conversor Euro -> Real') #Exibe a funciuonalidade do programa
euro_str = input('Insira o valor em euros: ') #Recebe o valor original
euro_str = euro_str.replace(',', '.') #Trata erros de digitação
euro = float(euro_str) #Transforma em float

real = euro * 5.4355 #Calcula com valor base 14/10/23
print(f'O valor após convertido é R${real:.2f}') #Exibe o valor em reais formatado