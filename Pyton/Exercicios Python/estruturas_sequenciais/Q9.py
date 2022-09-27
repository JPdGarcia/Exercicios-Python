#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).


print("Vamos converter uma temperatura em Fahrenheit para graus Celsius")
fahrenheitStri = input("Digite uma temperatura em Fahrenheit: ")

fahrenheit = float(fahrenheitStri)

celsius = 5*((fahrenheit-32)/9)
celsiusInt = int(celsius)

print("A temperatura digitada é: ", celsiusInt,"C°")