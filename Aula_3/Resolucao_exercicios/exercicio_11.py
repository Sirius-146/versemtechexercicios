# Exercício 11:

salario_atual = input('Salário atual: ').replace(',','.')
salario_atual = float(salario_atual)

novo_salario = None #Valor do novo salário

valor = [280, 700, 1500] #Valores atuais

mais = [0.20, 0.15, 0.10, 0.05] #Percentual de aumento
#Conferência de valores
aumento20 = salario_atual <= valor[0]
aumento15 = salario_atual < valor[1]
aumento10 = salario_atual < valor[2]
aumento5 = salario_atual > valor[2]

if aumento20:
  percentual = mais[0]
  aumento = salario_atual * percentual
  novo_salario = salario_atual + aumento
elif aumento15:
  percentual = mais[1]
  aumento = salario_atual * percentual
  novo_salario = salario_atual + aumento
elif aumento10:
  percentual = mais[2]
  aumento = salario_atual * percentual
  novo_salario = salario_atual + aumento
else:
  percentual = mais[3]
  aumento = salario_atual * percentual
  novo_salario = salario_atual + aumento

print(f'''Salário atual: {salario_atual} \nPercentual de aumento: {int(percentual * 100)}%
      \nValor de aumento: {aumento} \nSalário reajustado: {novo_salario}''')