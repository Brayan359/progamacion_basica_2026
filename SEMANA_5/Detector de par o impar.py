#Algoritmo
#pedir numero entero
#si el numero es divisible entre 2 es par
#si el numero no es divisible entre 2 no es par

#Pseudocodigo
#Inicio
#Leer numero
#resultado numero%2==0
#escribir if ("el numero es par")
#escribir else ("el numero es impar")
#Fin


numero=int(input("ingrese un numero entero"))
if numero%2==0:
    print("el numero es par.")
else:
    print("el numero es impar.")
