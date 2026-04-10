temp = float(input("temperatura en grados celsius"))

if temp <=0 :
    print("congelada")
elif temp >= 0 and temp <= 15 :
    print("fria")
elif temp >= 15 and temp <= 25 :
    print("TEMPERATURA: temperatura ideal")
elif temp >=25 and temp <= 35 :
    print("CALIDA")
else :
    print("EXTREMO CALOR")
