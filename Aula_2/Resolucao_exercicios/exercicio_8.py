# Exercício 8:

salario_hora_str = input('Insira o salário por hora: ') #Recebe o valor do salário horário
salario_hora_str = salario_hora_str.replace(',', '.') #Trata erros de digitação
salario_hora = float(salario_hora_str) #Transforma em float

horas_mes = float(input('Insira a quantidade de horas trabalhadas no mês: ')) #Recebe o valor referente as horas trabalhadas

salario_mensal = salario_hora * horas_mes #Calcula o salário mensal

print(f'O sálario nesse mês é de: R${salario_mensal:.2f}') #Exibe o valor formatado do salário mensal