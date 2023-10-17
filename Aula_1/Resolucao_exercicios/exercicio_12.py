# Exercício 12:

segundos = int(input('Insira o valor em segundos: ')) #Recebe um valor qualquer em segundos

QTE_SEG_HORA = 3_600 #Total de segundos em uma hora
QTE_SEG_MIN = 60 #Total de segundos em um minuto

horas = segundos // QTE_SEG_HORA #Quantidade de horas nos segundos inseridos
resto_horas = segundos % QTE_SEG_HORA #Resto da divisão anterior

minutos = resto_horas // QTE_SEG_MIN #Quantidade de minutos no resto da divisão anterior
segundo = resto_horas % QTE_SEG_MIN #Resto da divisão anterior. Total de segundos restantes

#Exibe a quantidade de horas, minutos e segundos no valor inserido
print(f'O valor resulta em: {int(horas)} horas, {int(minutos)} minutos e {int(segundo)} segundos.')