# Exercício 12:

#calculando a hora trabalhada e valor da hora trabalhada
valor_hora = input('Insira o valor da sua hora trabalhada: ').replace(',', '.')
valor_hora = float(valor_hora)

total_horas = input('Insira o total de horas trabalhadas: ').replace(',', '.')
total_horas = float(total_horas)

salary = valor_hora * total_horas #Calcula o salário
salario_final = None #armazena o valor líquido do salário

valor_base = [900, 1500, 2500] #Salários base para incidencia das taxas de IR

INSS = 0.1 #desconto INSS (Obs: tá errado, o valor varia de acordo com o salário)
FGTS = 0.11 #valor a ser pago de FGTS
IR = [0.05, 0.10, 0.20] #porcentagem de desconto de IR, de acordo com o salário

#Testa a faixa de salário
salary_1 = salary <= valor_base[0]
salary_2 = salary <= valor_base[1]
salary_3 = salary <= valor_base[2]

#Calcula os descontos fixos
inss_desconto = salary * INSS
fgts_desconto = salary * FGTS

if salary_1:
  desconto = 0
  salario_final = 0
elif salary_2:
  desconto = IR[0]
  salario_final = salary * desconto
elif salary_3:
  desconto = IR[1]
  salario_final = salary * desconto
else:
  desconto = IR[2]
  salario_final = salary * desconto

print(f'''  Salário Bruto:             : R$ {salary:.2f}
  (-) IR ({(desconto*100):.0f}%)               : R$ {salario_final:.2f}
  (-) INSS (10%)             : R$ {inss_desconto:.2f}
  FGTS (11%)                 : R$ {fgts_desconto:.2f}
  Total de descontos         : R$ {(salario_final + inss_desconto):.2f}
  Salário Liquido            : R$ {salary - (salario_final + inss_desconto):.2f}
''')