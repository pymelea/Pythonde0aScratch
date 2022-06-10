'''
Crear la función "operación" que dados 3 números, divide el primer número entre la resta de los otros dos números

Utilizar la función creada con los números 5,4,2
Utilizar la función creada con los números 6,3,3

Utiliza el bloque try .. except para controlar cualquier posible error
'''

def operacion(numero1, numero2, numero3):
    resultado = numero1 / (numero2 - numero3)
    return resultado


numero1 = 6
numero2 = 4
numero3 = 3
try:
    resultado = operacion(numero1, numero2, numero3)
    print(resultado)
except:
    print("Error, los ultimos dos numeros tienen que ser diferentes")

print(operacion(5,4,2))
# print(operacion(6,3,3))
