"""
"""

# r es para archivo solo lectura
archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()

print(len(lineas))
print(lineas[0])
print("-------------------")
print(lineas[1])

for x in lineas:
    print(x[9])