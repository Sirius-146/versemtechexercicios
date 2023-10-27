# Exercício 13:

dia_num = int(input('Número do dia: ')) #Recebe o valor referente ao dia da semana desejado

#Cria um dicionário, no qual o número representa a chave e o dia o valor
dias = {
    1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"
}

#Percorre o dicionário dias com o método get
#Se o valor de dia_num for encontrado em uma chave, retorna o valor da chave
#Caso o valor não seja representado por nenhuma chave, retorna "Valor Inválido"
print(dias.get(dia_num, "Valor Inválido")) #Imprime o valor na tela