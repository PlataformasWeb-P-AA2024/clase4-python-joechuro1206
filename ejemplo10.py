"""
"""

# r es para archivo solo lectura
archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()

# lineas compresas guardad en l cada linea || usamos el split para partir por el separador convertimos las lineas en listas separadas por el pipe

lineas = [l.split("|") for l in lineas]

#inicializo un contador
contador = 1
# Ahora imprimira la posicion 9 de las listas partidas por el split
for x in lineas:
    cadena = """<b>Torneo:</b> %s <br> <b>Ganador: <b/>%s""" % (x[0], x[9])
    print(cadena)
    archivo_generado = open("data/%d_%s.html" % (contador, x[9]), "w")
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close
    # aumentamos el contador en cada iteracion el resultado seria 1_nombreganador hasta 25362
    contador += 1 
    #DEBEN SALIR 25362 ARCHIVOS
   