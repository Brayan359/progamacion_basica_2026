#preguntar si es estudiante
es_estudiante = (input("¿eres estudiante?,(si/no):"))

#Leer total de la compra
total = float(input("total de tu compra en pesos, $ :"))

if es_estudiante == "si" or total > 200000 :
        descuento = total * 0.15
        total_final = total - descuento
        print("Descuento aplicado del 15%")
        print("Descuento: $", descuento)
        print("Total a poagar:$",total)
else:
        print("sin descuento. total: $", total)
