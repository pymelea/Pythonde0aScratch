# Ejercicio

# A partir de la lista "numeros" que contiene números del 1 al 10,
# Obtener mediante "filter" una lista denominada "pares" con los numeros pares de la lista "numeros"


numeros = [1,2,3,4,5,6,7,8,9,10]

def par(numero):
    return (numero % 2 ) == 0


resultado = list(filter(par, numeros))
# pares = list(resultado)
# print(pares)
print(resultado)

