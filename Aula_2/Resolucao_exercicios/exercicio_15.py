# Exercício 15:

sal_hora_str = float(input('Insira o salário por hora: ')) #Recebe o valor do salário horário
sal_hora_str = sal_hora_str.replace(',', '.') #Trata erros de digitação
sal_hora = float(sal_hora_str) #Transforma em float

h_mes = float(input('Insira a quantidade de horas trabalhadas no mês: ')) #Recebe o valor referente as horas trabalhadas

salario_bruto = sal_hora * h_mes #Calcula o salário bruto mensal
IMPOSTO_RENDA = salario_bruto * 0.11 #Calcula o desconto de imposto de renda
INSS = salario_bruto * 0.08 #Calcula o desconto de INSS
SINDICATO =  salario_bruto * 0.05 #Calcula o desconto de sindicato

#Calcula o salário líquido, que equivale ao salário menos os descontos
salario_liquido = salario_bruto - IMPOSTO_RENDA - INSS - SINDICATO

#Imprime o resultado formatado ao usuário
print(f'''+ Salário Bruto : R${salario_bruto:.2f}
- IR (11%) : R${IMPOSTO_RENDA:.2f}
- INSS (8%) : R${INSS:.2f}
- Sindicato (5%) : R${SINDICATO:.2f}
= Salário Liquido : R${salario_liquido:.2f}''')