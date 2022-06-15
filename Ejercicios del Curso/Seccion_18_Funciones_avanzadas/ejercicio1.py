"""
Crear la funcion "primos" que será una funcion generadora  de números primos entre 0 y el 100
Esta es la lista de números  primos entre 0 y 100
numeros_primos = [ 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,97]

Utilizar la función generadora para mostrar por pantalla numeros primos menores de 50
""" 
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,97]

def primos(maximo):
    for numero in range(maximo):
        if (numero in numeros_primos):
            yield numero

        if (numero > 100):
            break


maximo = 50
for numero in primos(maximo) :
    print(numero)

# list(primos(numeros_primos))
# print(resultado)

