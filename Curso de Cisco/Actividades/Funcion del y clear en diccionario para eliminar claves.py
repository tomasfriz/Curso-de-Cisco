polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

print(len(polEspDict))    # salida: 3
del polEspDict["zamek"]    # elimina un elemento
print(len(polEspDict))    # salida: 2

polEspDict.clear()   # elimina todos los elementos
print(len(polEspDict))    # salida: 0

del polEspDict    # elimina el diccionario