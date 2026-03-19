#Algoritmo
#Pedir valor de la compra
#Si el valor es mayor >100.000 tiene descuento del 15%
#calcular 100.000*0.85
#Si el valor es menor a <100.000 no tiene descuento
#100.000 exacto no tiene descuento

#Pseudocodigo
#inicio
#leer valor de compra
#resultado compra>100.000*0.85
#escribir "tiene descuento del 15%"
#resultado <100.000
#escribir "no tiene descuento"

precio_inicial=int(input("Digite el valor de la compra"))
if precio_inicial>100000:
    descuento=precio_inicial*0.15
    precio_final=precio_inicial-descuento
    print(f"tiene descuento del 15%:$",descuento)
    print(f"precio final:$",precio_inicial)
else:
    print("precio final:$",precio_inicial,"(no aplica descuento)")
