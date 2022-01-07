variable1 = 1
variable2 = 2

auxiliar = variable1
variable1 = variable2
variable2 = auxiliar 

print(variable1)
print(variable2)

#-------------------------------------------

variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1 

print(variable1)
print(variable2)