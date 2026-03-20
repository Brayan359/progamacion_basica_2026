#Algoritmo
#Leer datos del viaje
#inicilizar el costo
#aplicar recargo nocturno
#calcular costo por kilometro

#Pseudocodigo
#Inicio
#Leer distancia,hora
#costo=5000
#resultado hora >=21 o hora <5
#si costo = costo*1.3
#no: continuar
#distancia>10
#si: costo = costo + (distancia-10)*800
#no: continuar
#mostrar costo
#terminar

print("Ingrese los datos del viaje:")
distancia = float(input("Distancia en km: "))
hora = int(input("Hora del día (0-23): "))
    
tarifa_base = 5000
costo = tarifa_base
    
# Recargo nocturno
if hora >= 21 or hora < 5:
   costo *= 1.3
print("Recargo nocturno aplicado")
    
    # Costo por kilómetro adicional
if distancia > 10:
   costo += (distancia - 10) * 800
    
print("Costo total del viaje: $", round(costo))
