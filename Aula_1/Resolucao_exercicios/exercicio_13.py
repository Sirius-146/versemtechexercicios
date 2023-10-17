# Exercício 13:

tanque = float(input('Digite a quantidade de combustível no tanque: ')) #Recebe a quantidade de combustível no tanque
consumo = float(input('Digite o consumo médio do carro: ')) #Recebe o valor de consumo médio do veículo

km = tanque * consumo #Calcula a quantidade de quilometros que o veículo ainda pode rodar com esse combustível

print(f'Com esse combustível você pode percorrer {km}Km') #Exibe o valor de quilometros