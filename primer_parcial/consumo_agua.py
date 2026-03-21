#Algoritmo
#Pedir nombre del usuario
#pedir al usuario el consumo de agua en metros(numero entero)
# si el consumo es bajo debe ser menor o igual 0
#si el consumo es normal debe ser menor o igual a 15
#si el consumo es alto debe ser mayor a 30



#Pseudocodigo
#Leer nombre del usuario
#Leer consumo de agua(numero entero)
#resultado consumo <=0
#escribir("Error: el consumo debe ser mayor a 0")
#resultado consumo <=15
#escribir ("Excelente! Eres un usuario responsable del agua")
#resultado consumo <=30
#escribir ("Tu consumo está dentro del promedio del hogar")
#escribir No: ("Atención: tu consumo es alto, revisa posibles fugas")

nombre=input("Digite su nombre")
consumo=int(input("Digite el consumo de agua"))
if consumo <=0:
    print("Error: el consumo debe ser mayor a 0")
elif consumo <=15:
    print("Excelente! Eres un usuario responsable del agua")
elif consumo <=30:
    print("Tu consumo está dentro del promedio del hogar")   
else:
    consumo 
    print("Atención: tu consumo es alto, revisa posibles fugas") 
