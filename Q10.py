#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


print("Vamos converter uma temperatura em graus Celsius para Fahrenheit")
celsiusStr = input("Digite uma temperatura em graus Celsius: ")

celsius = float(celsiusStr)

fahrenheit = (celsius* 9/5)+32
fahrenheitInt = int(fahrenheit)

print("A temperatura digitada é:", fahrenheitInt, "F°")
