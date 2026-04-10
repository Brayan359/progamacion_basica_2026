# leer carnet
# escribir "tiene pase de invitado, (si/no):"
#leer invitado
#escribir "¿viene con socio?, (si/no):"
#leer socio 
# si edad es >= 14 Y (carnet == "si" O invitado = "si" o socio = "si" entonces
# escribir " bienvendio al gimnasio
# siNo 
# escribir "acceso denegado"

edad = int(input(" ¿que edad tiene?"))

carnet = (input("¿tiene carnet de afiliado?, (si/no):"))

invitado = (input("¿tiene pase de invitado?, (si/no):"))

socio = (input("¿viene con socio?, (si/no)"))

if edad <= 14 and (carnet == "si" or invitado == "si" or socio == "si"): 
    print("bienvenido al gimnasio")
else :
    print("acceso denegado")
