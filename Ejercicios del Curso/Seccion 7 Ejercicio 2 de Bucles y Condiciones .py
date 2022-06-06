'''
Creamos una variable "nota" que tenga el valor 4.5
Creamos una variable "trabajo_realizado" que tenga el valor "SI"
Calcular el valor de la variable "nota_final", teniendo en cuenta que , si la nota final es mayor o igual a 4,
y el valor de la variable "trabajo_realizado" es igual a "si", entonces "nota_final"
sera igual a "aprobado, en caso contrario sera igual a "suspenso"

'''

nota = 4.5
trabajo_realizado = "SI"

if (nota >= 4) and (trabajo_realizado == "SI"):
    nota_final = "aprobado"
else:
    nota_final = "suspenso"
print(nota_final)