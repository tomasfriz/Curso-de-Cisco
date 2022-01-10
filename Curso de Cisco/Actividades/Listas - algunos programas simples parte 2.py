miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5 #El valor buscado se almacena en la variable Encontrar.
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar #El estado actual de la búsqueda se almacena en la variable Encontrado (True/False).
    if Encontrado: #Cuando Encontrado se convierte en True, se sale del bucle for.
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
#-----------------------------------------------------------------------------------------    
sorteados = [5, 11, 9, 42, 3, 49] #La lista sorteados almacena todos los números ganadores.
seleccionados = [3, 7, 11, 42, 34, 49] #La lista de seleccionados almacena con números con que se juega.
aciertos = 0 #La variable aciertos cuenta tus aciertos.

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)