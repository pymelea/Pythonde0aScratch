# Ejercicio

# A partir de una lista de números del 1 al 10,
# Obtener una nueva lista con todos los elementos incrementados en 10 unidades


numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def incrementar(numero):
    resultado = numero + 10 
    return resultado

print(incrementar(5))

resultado = map(incrementar, numero)
mapeo = list(resultado)
print(mapeo)

