#Algoritmo
#mostrar menu con un si o un no
#mostar menu universitario
#poner bandeja $18.000
#poner ajiaco $15.000
#poner sancocho 12.000
#opcion para ingresar con numero 
#poner opcion 1,2 y 3 si desean alguna opcion.
#si ponen mal la opcion envia error

#Pseudocodigo
#inicio
#Leer si acepta
#escribir "menu del restaurante"
#escribir "1 bandeja paisa $18.000"
#escribir "2 ajiaco $15.000"
#escribir "sancocho $12.000"
#Leer numero
#resultado opcion==1
#escribir "ha elegido bandeja paisa. total: $18.000" 
#resultado opcion==2
#escribir"ha elegido ajiaco. total: $15.000"
#resultado opcion==3
#escribir"ha elegido sancocho. total: $12.000"
#escribir else: "opcion invalida.porfa vor intente de nuevo"

mostrar_menu=(input("Quieres ver el menu"))
print("Menú del Restaurante Universitario")
print("1. Bandeja Paisa ($18.000)")
print("2. Ajiaco ($15.000)")
print("3. Sancocho ($12.000)")

opcion = int(input("Ingrese el número de su opción: "))
if opcion == 1:
        print("Ha elegido Bandeja Paisa. Total: $18.000")
elif opcion == 2:
        print("Ha elegido Ajiaco. Total: $15.000")
elif opcion == 3:
        print("Ha elegido Sancocho. Total: $12.000")
else:
        print("Opción inválida. Por favor, intente de nuevo.")
