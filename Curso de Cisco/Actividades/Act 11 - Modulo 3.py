c0 = int(input("Ingrese c0: "))

if c0 > 1:
    pasos = 0
    while c0 != 1:
        if c0 %2 != 0:
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2
        c0 = cnew
        pasos += 1
        print(c0)
    print("pasos =", pasos)
else:
        print("Valor de c0 incorrecto")