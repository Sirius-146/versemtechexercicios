# Exercício 11:

salario_atual = input('Salário atual: ').replace(',','.') #Recebe um valor e, caso haja vírgula, troca por ponto
salario_atual = float(salario_atual) #Transforma o valor recebido e reformatado em float

novo_salario = None #Valor do novo salário

valor = [280, 700, 1500] #Valores atuais

mais = [0.20, 0.15, 0.10, 0.05] #Percentual de aumento
#Conferência de valores
aumento20 = salario_atual <= valor[0]
aumento15 = salario_atual < valor[1]
aumento10 = salario_atual < valor[2]
aumento5 = salario_atual > valor[2]

if aumento20: #Testa se o retorno da variável é verdadeiro
  percentual = mais[0] #Recebe a porcentagem de aumento de acordo com o salário atual
  aumento = salario_atual * percentual #Calcula o valor do aumento
  novo_salario = salario_atual + aumento #Soma o valor de aumento ao salário
elif aumento15: #Testa se o retorno da variável é verdadeiro
  percentual = mais[1] #Recebe a porcentagem de aumento de acordo com o salário atual
  aumento = salario_atual * percentual #Calcula o valor do aumento
  novo_salario = salario_atual + aumento #Soma o valor de aumento ao salário
elif aumento10: #Testa se o retorno da variável é verdadeiro
  percentual = mais[2] #Recebe a porcentagem de aumento de acordo com o salário atual
  aumento = salario_atual * percentual #Calcula o valor do aumento
  novo_salario = salario_atual + aumento #Soma o valor de aumento ao salário
else: #Caso o valor seja falso
  percentual = mais[3] #Recebe a porcentagem de aumento de acordo com o salário atual
  aumento = salario_atual * percentual #Calcula o valor do aumento
  novo_salario = salario_atual + aumento #Soma o valor de aumento ao salário

#Imprime o valor na tela
print(f'''Salário atual: {salario_atual} \nPercentual de aumento: {int(percentual * 100)}%
      \nValor de aumento: {aumento} \nSalário reajustado: {novo_salario}''')