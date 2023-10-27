# Exercício 12:

#calculando a hora trabalhada e valor da hora trabalhada
valor_hora = input('Insira o valor da sua hora trabalhada: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
valor_hora = float(valor_hora) #Transforma o valor recebido e reformatado em float

total_horas = input('Insira o total de horas trabalhadas: ').replace(',', '.') #Recebe um valor e, caso haja vírgula, troca por ponto
total_horas = float(total_horas) #Transforma o valor recebido e reformatado em float

salary = valor_hora * total_horas #Calcula o salário
salario_final = None #armazena o valor líquido do salário

valor_base = [900, 1500, 2500] #Salários base para incidencia das taxas de IR

INSS = 0.1 #desconto INSS de acordo com o enunciado
FGTS = 0.11 #valor a ser pago de FGTS
IR = [0.05, 0.10, 0.20] #porcentagem de desconto de IR, de acordo com o salário

#Testa a faixa de salário
salary_1 = salary <= valor_base[0]
salary_2 = salary <= valor_base[1]
salary_3 = salary <= valor_base[2]

#Calcula os descontos fixos
inss_desconto = salary * INSS
fgts_desconto = salary * FGTS

if salary_1: #Testa se o retorno da variável é verdadeiro
  desconto = 0 #Não há desconto
  salario_final = 0 #Não há alteração no valor final
elif salary_2: #Testa se o retorno da variável é verdadeiro
  desconto = IR[0] #O desconto é calculado com o valor salvo na posição 0 da lista
  salario_final = salary * desconto #Calcula o desconto a ser apliocado no salário final
elif salary_3: #Testa se o retorno da variável é verdadeiro
  desconto = IR[1] #O desconto é calculado com o valor salvo na posição 1 da lista
  salario_final = salary * desconto #Calcula o desconto a ser apliocado no salário final
else: #Caso o valor seja falso
  desconto = IR[2] #O desconto é calculado com o valor salvo na posição 2 da lista
  salario_final = salary * desconto #Calcula o desconto a ser apliocado no salário final

#Imprime o valor na tela
print(f'''  Salário Bruto:             : R$ {salary:.2f}
  (-) IR ({(desconto*100):.0f}%)               : R$ {salario_final:.2f}
  (-) INSS (10%)             : R$ {inss_desconto:.2f}
  FGTS (11%)                 : R$ {fgts_desconto:.2f}
  Total de descontos         : R$ {(salario_final + inss_desconto):.2f}
  Salário Liquido            : R$ {salary - (salario_final + inss_desconto):.2f}
''')