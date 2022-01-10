vehiculosUno = ['carro', 'bicicleta', 'moto']
print(vehiculosUno) # salida: ['carro', 'bicicleta', 'moto']

vehiculosDos = vehiculosUno
del vehiculosUno[0] # borra 'carro'
print(vehiculosDos) # salida: ['bicicleta', 'moto']
