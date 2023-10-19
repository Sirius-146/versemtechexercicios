# Exercício 10:

temp_celsius_str = input('Insira a temperatura em Celsius: ') #Recebe o valor da temperatura em Celsius
temp_celsius_str = temp_celsius_str.replace(',', '.') #Trata erros de digitação
temp_celsius = float(temp_celsius_str) #Transforma em float

#O valor em Fahrenheit equivale a temperatura em Celsius dividido por 5, sendo em seguida multiplicado por 9 e então adicionado 32
temp_convert_fahrenheit = (temp_celsius / 5) * 9 + 32 #Calcula a conversão de temperatura

#Exibe a temperatura original e seu valor convertido
print(f'{temp_celsius}°C convertidos para Fahrenheit são {temp_convert_fahrenheit}°F')