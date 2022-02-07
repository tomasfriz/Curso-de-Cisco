print("Me gusta ser un módulo.")
print(__name__)

if __name__ == "__main__":
    print("prefiero ser un modulo")
else:
    print("me gusta ser un modulo")

#!/usr/bin/env python3 

""" module.py - un ejemplo de módulo de Python """

__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__":
	print("Prefiero ser un módulo, pero puedo hacer algunas pruebas para ti.")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)
