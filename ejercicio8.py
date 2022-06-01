'''
Crea una variable "minimo" con el valor 20
Crea una variable "maximo" con el valor 500
Recoge un valor del  teclado  y almacenelo en la variable "dato"
Convierte la variable  "dato" en un número y almacenelo en la variable "numero"
Si el "numero" es menor que el valor de "minimo" mostrar el texto "Valor bajo"
Si el "numero" es mayor que el valor de "maximo" mostrar el texto "Valor alto"
Si el "numero" está entre el valor de "minimo"  y "maximo", mostrar "Valor medio"
'''

minimo = 20
maximo = 500

dato = input("Introduce un valor: ")
numero = int(dato)

if numero < minimo:
    print("Valor bajo")

elif numero > maximo:
    print("Valor alto")

else:
    print("Valor medio")
