'''
Crear una variable "inicio" con el valor 1
Crear una variable "fin" con el valor 6
Hacer un bucle while que muestre tantas filas como valores haya entre "inicio" y "fin"
En cada iteracion del bucle mostrar el texto "Esta es la fila" + numero de la fila en la que está
'''

inicio = 1
fin = 6
while (inicio < fin) :
    print("Esta es la fila " + str(inicio))
    inicio = inicio + 1