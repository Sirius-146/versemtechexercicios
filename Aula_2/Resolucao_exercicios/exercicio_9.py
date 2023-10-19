# exercício 9:

temp_fahrenheit_str = input('Insira a temperatura em Fahrenheit: ') #Recebe o valor da temperatura em Fahrenheit
temp_fahrenheit_str = temp_fahrenheit_str.replace(',', '.') #Trata erros de digitação
temp_fahrenheit = float(temp_fahrenheit_str) #Transforma em float

#O valor em Celsius equivale a temperatura em Fahrenheit menos 32, sendo em seguida dividido por 9 e então multiplicado por 5
temp_convert_celsius = 5 * ((temp_fahrenheit-32) / 9) #Calcula a conversão de temperatura

#Exibe a temperatura original e seu valor convertido
print(f'{temp_fahrenheit}°F convertidos para Celsius são {temp_convert_celsius}°C')