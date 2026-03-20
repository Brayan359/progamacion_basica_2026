#Algoritmo
#Leer kla nota numerica
#verificar si la nota es valida.
#clasificar la nota
#verificar si requiere habilitacion

#Pseudocodigo
#inicio
#leer nota
#resultado nota<0.0 o nota>5.0
# escribir si: nota invalida
# escribir no: continuar 
#resultado nota >=4.5
#escribir si: A excelente
#resultado no: >= 4.0
#escribir si: B sobresaliente
#resultado no: >= 3.5
#escribir: si: C-Bueno
#resultado: no: nota >=3.0
#escribir si: D-aceptable
#escribir no: E-reprobado
#resultado nota>=2.0 y nota <3.0
#escribir si: requiere habilitacion
#escribir no: no requiere habilitacion
#Fin



nota = float(input("Ingrese la nota numérica (0.0 a 5.0): "))

if nota < 0.0 or nota > 5.0:
        print("Nota inválida. Debe estar entre 0.0 y 5.0")
elif nota >= 4.5:
        print("Nota: A - Excelente")
elif nota >= 4.0:
        print("Nota: B - Sobresaliente")
elif nota >= 3.5:
        print("Nota: C - Bueno")
elif nota >= 3.0:
        print("Nota: D - Aceptable")
else:
        print("Nota: E - Reprobado")
        
        if nota >= 2.0:
            print("Requiere habilitación")
        else:
            print("No requiere habilitación")
