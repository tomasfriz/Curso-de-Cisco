﻿def potenciasDe2(n):
    potencia= 1
    for i in range(n):
        yield potencia
        potencia*= 2

for i in range(20):
    if i in potenciasDe2(4):
        print(i)