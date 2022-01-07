miLista  = [1, 1, None, True, 'Soy una cadena', 256, 0]
print(miLista [3]) # salida: soy una cadena
print(miLista  [-1]) # salida: 0

miLista  [1] = '?'
print (miLista) # salida: [1, '?', True, 'Soy una cadena', 256, 0]

miLista.insert (0, "first")
miLista.append ("last")
print (miLista ) # salida: ['first', 1, '?', True, 'Soy una cadena', 256, 0, 'last'] 
