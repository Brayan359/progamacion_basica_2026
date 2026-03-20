#Algoritmo
#Leer lado de los triangulos
#verificar si los lados forman un triangulo
#clasificar el triangulo
# si cumple com la primera condicion es un triangulo
#si cumple la segunda condicion es equilatero 
#si cumple la tercera condcion es isoceles
# si no cumple es escaleno
#si no cumplen las condiciones es los lados no forman un triangulo.

#Pseudocodigo
#inicio
#leer lado 1, lado 2, lado 3
#¿(lado1+lado2>lado3)y(lado1+lado3>lado2)y(lado2+lado3>lado1)?
#si:los lados forman un triangulo
#no: los lados no forman un triangulo
#¿(lado==lado2==lado3)?
#si isosceles
#no: no escaleno
#terminar

print("Ingrese los lados del triángulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Los lados forman un triángulo.")
    if lado1 == lado2 == lado3:
      print("Clasificación: Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
      print("Clasificación: Isósceles")
    else:
      print("Clasificación: Escaleno") 
else:
    print("Los lados no forman un triángulo.")
