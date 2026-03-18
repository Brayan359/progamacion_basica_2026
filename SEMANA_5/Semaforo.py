#Algoritmo
#Pedir color de semaforo 
#Si es verde puede seguir
#Si es rojo detente
#Si es amarillo es alerta

#Pseudocodigo
#Leer color de semaforo
#Resultado semaforo==verde
#Escribir "puedes seguir"
#Resultado semaforo==rojo
#Escribir "detente"
#Resultado semaforo== amarillo
#Escribir "alerta"
#Fin


semaforo=input("Dame el color del semaforo")
if semaforo=="verde":
    print("puedes seguir")
elif semaforo=="rojo":
    print("detente")
elif semaforo=="amarillo":
    print("alerta")
