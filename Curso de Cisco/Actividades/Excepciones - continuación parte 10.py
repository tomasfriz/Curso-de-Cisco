try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!") #no colocar antes excepciones generales antes de excepciones concretas.
except ZeroDivisionError:
    print("¡División entre Cero!") #nunca se utilizara esta excepcion.

print("FIN.")