#Algoritmo
#Pedir edad del usuario
#pedir si o no el usuario tiene licencia
#si el usuario es mayor o igual años y tiene licencia puede manejar
#si no tiene 18 y no tiene licencia no puede manejar

#Pseudocodigo
#inicio
#escribir "ingresa edad"
#leer edad
#escribir "tienes licencia vigente (si/no):"
# Leer tiene_licencia
#Si edad >= 18 Y tiene_licencia = 'si' Entonces
#Escribir 'Puedes conducir. Maneja con cuidado!'
#SiNo
#Escribir 'No puedes conducir.'
#FinSi


edad = int(input("cual es tu edad"))

licencia=(input("tienes licencia vigente, (si / no):"))

if edad>=18 and licencia == "si" :
    print("¡puedes conducir, maneja con cuidado")
else:
    print("No puedes conducir, necesitas tener al menos 18 años y una licencia vigente")
