# Paso 1:
Beatles = []
print("Paso 1:", Beatles)

# Paso 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# Paso 3:
for miembros in range(2):
    Beatles.append (input ("Nuevo miembro de la banda:"))
print("Paso 3:", Beatles)

# Paso 4:
del Beatles [-1]
del Beatles [-1]
print("Paso 4:", Beatles)

# Paso 5:
Beatles.insert (0, "RingoStarr")
print("Paso 5:", Beatles)
print("Los Fab:", len (Beatles))