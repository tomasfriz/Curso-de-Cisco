polEspDict = {"kwiat" : "flor"}

polEspDict.update({"gleba" : "tierra"})
print(polEspDict)    # salida: {'kwiat' : 'flor', 'gleba' : 'tierra'}

polEspDict.popitem()
print(polEspDict)    # outputs: {'kwiat' : 'flor'}