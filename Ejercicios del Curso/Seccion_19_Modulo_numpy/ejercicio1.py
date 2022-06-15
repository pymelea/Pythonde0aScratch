# Ejercicio

# Crear la función "pares"  que devuelva una array de números entre los valores pasados como parámetros a la función (inicio y fin)
# Utilizar la función "pares" con los números del 1 al 30
# Utilizar la función "pares" con los números del 2 al 40

import numpy as np

# def pares(inicio, fin):
#     return np.arange(inicio, fin+1, 2)  # arange devuelve un array de números entre inicio y fin

# def pares(fin, i):
#     return np.arange(fin+1, i+1, 2)  # arange devuelve un array de números del 1 al 30

def pares(inicio, fin):
    if (inicio % 2 ==  0):
       array = np.arange(inicio, fin, 2) 
    else:
        inicio = inicio + 1
        array = np.arange(inicio, fin, 2) 
    return array

print(pares(1, 30))
print(pares(2, 40))


