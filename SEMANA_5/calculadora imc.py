#Algoritmo
#Pedir peso
#Pedir altura
#calcular el peso por la altura
#dar imc del usuario correspondiente
#si el imc es <18.5 es bajo peso
#si el imc es mayor o igual a 18.5 y si es <=24.9 es de peso normal
#si el imc es mayor o igual a 25 y menor o igual a 29 es sobrepreso
#si es mayor 29.9 es obesidad

#Pseudocodigo
##Inicio
#Leer peso
#Leer altura
#Resultado imc=peso/(altura**2)
#Resultado if imc< 18.5
#Escribir "clasifiacion: bajo peso"
#Calcular  elfi imc >= 18.5 and imc <24.9
#Escribir "clasifiacion normal"
#Calcular elif >= 25 and imc <= 29.9
#Escribir "clasificacion obesidad"
#Escribir else "clasifiacion obesidad"

#calcular_imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("Su IMC es: ", imc)

if imc < 18.5:
        print("Clasificación: Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
        print("Clasificación: Normal")
elif imc >= 25 and imc <= 29.9:
        print("Clasificación: Sobrepeso")
else:
        print("Clasificación: Obesidad")
