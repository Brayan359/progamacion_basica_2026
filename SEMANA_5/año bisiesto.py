#Algoritmo
#Leer el año
#Verificar si el año es divisible entre
# Si no, no es bisiesto
#Verificar si el año es divisible entre 100
# Si no, es bisiesto
# Si sí, verificar si es divisible entre 400
# Si sí, es bisiesto
# Si no, no es bisiesto

#Psedocodigo
#Inicio
# Leer año
# año % 4 == 0?
# No: No es bisiesto -> 7
# Sí: Continuar
# año % 100 == 0?
# No: Es bisiesto -> 7
# Sí: Continuar
# año % 400 == 0?
# No: No es bisiesto -> 7
# Sí: Es bisiesto
# Mostrar resultado
# Fin


año = int(input("Ingrese un año: "))
    
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
   print(año, "es un año bisiesto")
else:
   print(año, "no es un año bisiesto")
