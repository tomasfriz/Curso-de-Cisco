bloques = int(input("Ingrese el número de bloques: "))

altura = 0
capa = 1
while capa <= bloques:
	altura += 1
	bloques -= capa
	capa += 1
print("La altura de la pirámide:", altura)