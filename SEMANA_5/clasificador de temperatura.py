#Algoritmo
#pedir temperatura en °c
#si la temperatura es menor a 5°c hace mucho frio
#si la temperatura es mayor o igual 5°c y es menor o igual a 14°c es frio
#si la temperatura es mayor o igual a 15°c y menor o igual a 24°c es templado
#si la temperatura es mayor o igual 25°c y menor o igual a 34°c es caliente
#si la temperatura es mayor 34°c es muy caliente.

#Pseudocodigo
#inicio
#leer temperatura
#resultado if temperatura>=5 and temperatura<=14
#escribir ("muy frio")
#resultado elif temperatura>=15 and temperatura<=24
#escribir ("frio")
#resultado elif temperatura>=25 and temperatura<=34
#escribir ("caliente")
#resultado else temperatura >34
#escribir ("muy caliente")



temperatura=float(input("ingrese la temperatura en °c:"))
if temperatura<5:
    print("muy frio")
elif temperatura>=5 and temperatura<=14:
    print("Frio")
elif temperatura>=15 and temperatura<=24:
    print("templado")
elif temperatura>=25 and temperatura<=34:
    print("caliente")
else:
    print("muy caliente")
