# Exercício 18:

tamanho_arquivo = float(input('Insira o tamanho do arquivo (Mb): ')) #Recebe o valor do tamanho do arquivo
velocidade_internet = float(input('Insira a velocidade da internet (Mbps): ')) #Recebe o valor da velocidade da internet

velocidade_mbpm = velocidade_internet * 60 #Converte a velocidade da internet para Mb por minuto
tempo = tamanho_arquivo / velocidade_mbpm #Calcula o tempo para download

#Exibe o tempo de download ao usuário
print(f'O download deve levar {tempo} minuto(s)')