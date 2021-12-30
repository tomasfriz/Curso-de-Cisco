hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

min += dura # encuentra el total de minutos
hora += min // 60 # encuentra el número de horas ocultos en los minutos y actualiza las horas
min %= 60 # corrige los minutos para que estén en un rango de (0..59)
hora %= 24 # corrige las horas para que estén en un rango de (0..23)

print(hora, ":", min, sep='')