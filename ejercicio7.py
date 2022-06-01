'''
Crear una variable "nota1" que tenga el valor 6
Crear una variable "nota2" que tenga el valor 4
Crear una variable "nota3" que tenga el valor 7
Crear una variable "nota_media" que tenga el valor medio de las 3 notas anteriores
Crear una variable "nota_final" que tenga el valor "aprobado" (mayor o igual a 5)
'''

nota1 = 6
nota2 = 4
nota3 = 7
nota_media = (nota1 + nota2 + nota3) / 3
if (nota_media >= 5):
    nota_final = "aprobado"
    print(nota_final)

nota_final = "aprobado" if nota_media >= 5 else "suspendido"
print(nota_final)
