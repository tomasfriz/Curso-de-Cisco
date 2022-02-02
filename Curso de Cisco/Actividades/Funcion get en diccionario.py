polEspDict = {
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

elemento1 = polEspDict["gleba"]    # ejemplo 1
print(elemento1)    # salida: tierra

elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua