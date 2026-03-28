#Algoritmo
#Pedir usuario 
#pedir contraseña
#si el usuario es correcto y es correcta la contraseña puede acceder
#si el usuario es incorrecto y la contraseña es incorrecta no puede acceder


usuario = input("cual es tu usuario")
contraseña = int(input("cual es tu contraseña"))

if usuario == "admin" and contraseña == 1234 :
    print("acceso concidido. bienvenido")
    print("cargando tu perfil")
else:
    print(" acceso denegado")
