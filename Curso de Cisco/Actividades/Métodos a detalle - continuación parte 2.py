﻿# ejemplos de prueba aquí

class conClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = conClase()
obj.metodo()