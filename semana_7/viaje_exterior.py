pasaporte =(input("¿Tienes pasaporte vigente?, (si/no):"))

visa = (input("¿tienes visa?, (si/no):"))

exento = (input("¿tu pais esta exento de visa?, (si/no):"))
if pasaporte == "si" and (visa == "si" or exento == "si"):
    print("puedes viajar. buen viaje")

else:
    print("no puedes viajar. revisa tus documentos.")
