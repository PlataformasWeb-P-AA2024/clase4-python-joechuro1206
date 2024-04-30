sueldo = int(input("Ingrese sueldo de persona:"))

if sueldo <= 100:
    print("Correcto")
else:
    if(sueldo >= 101) and (sueldo <=110):
        print("Sobresaliente")
    else:
        print("Incorrecto")