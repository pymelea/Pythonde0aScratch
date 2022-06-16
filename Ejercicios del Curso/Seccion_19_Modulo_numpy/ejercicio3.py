# Ejercicio 3

# Crear una lista con los valores numéricos del 0 al 30
# Crear otra lista con los primeros 10 valores de la lista inicial
# Crear otra lista con los ultimos 10 valores de la lista inicial
# Crear un bucle que recorra esta ultima lista de valores finales
import numpy as np

lista1 = np.arange(0, 30)

lista_primeros = lista1[:10]
print(lista_primeros)

lista_ultimos = lista1[-10:]
print(lista_ultimos)

for ultimos in lista_ultimos:
    print(ultimos)
