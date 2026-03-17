#Algoritmo
#Digitar numero entero
#Si el  numero es mayor o igual a 0 es positivo.
#Si no es mayor o igual que 0 es negativo
#Si es igual 0 es neutro

#Pseudocodigo
#Inicio
#Leer numero
#Resultado >0
#Escribir "es positivo"
#Resultado <0
#Escribir "es igual 0"
#Escribir "si es igual 0 es neutro"
#Fin


numero=int(input("digite un numero entero"))
if numero>0:
    print("es positivo")
elif numero<0:
    print(" es igual a 0")

else:
    print("es neutro")
