diccionario = {}

diccionario['nombres'] = "Joe Miguel"
diccionario['apellidos'] = "Churo Calderon"
diccionario['ciudad'] = "Loja"

print(diccionario.keys())

print(diccionario['apellidos'])

print("--------------")

for x in diccionario.keys():
    print(diccionario[x])