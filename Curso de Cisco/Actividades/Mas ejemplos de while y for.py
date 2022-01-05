# Ejemplo 1
print("Ejemplo 1")
while True:
    print("Atascado en un ciclo infinito")
    break

# Ejemplo 2
print("Ejemplo 2")
contador = 5
while contador > 2:
    print(contador)
    contador -= 1

# Ejemplo 3
print("Ejemplo 3")
palabra = "Python"
for letra in palabra:
    print(letra, end= "*")

# Ejemplo 4
print("")
print("Ejemplo 4")
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# Ejemplo 5
print("Ejemplo 5")
texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end= "")

# Ejemplo 6
print("")
print("Ejemplo 6")
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")

# Ejemplo 7
print("")
print("Ejemplo 7")
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
    
print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

# Ejemplo 8
print("Ejemplo 8")
for i in range(3):
    print(i, end=" ") # salidas: 0 1 2
print("")
for i in range(6, 1, -2):
    print(i, end=" ") # salidas: 6, 4, 2
