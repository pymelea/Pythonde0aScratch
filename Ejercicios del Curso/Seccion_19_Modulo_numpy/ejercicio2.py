# Ejercicio

# Crear una lista con números del 10 l 19
# Crear otra lista con números del 50 al 59
# Crear una matriz 2x10 con las listas anteriores
# Crear una matriz que cuyos valores sean iguales a la matriz anterior multiplicados por 2

import numpy as np

# lista1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
lista1 = np.arange(10, 20)

# lista2 = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
lista2 = np.arange(50, 60)
lista_doble = (lista1,lista2)

matriz = np.array(lista_doble)

matriz_mult = matriz * 2


print(matriz)
print(matriz_mult)
