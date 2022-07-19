# Calcular el numero de botes de pintura que hacen falta para pintar una pared
# Pediremos al usuario
#   Alto de la pared
#   Ancho de la pared
#   Cuantos metros cuadrados cubre un bote de pintura
# Crearemos una función que calcule el numero de botes
# Formula = (Alto * Ancho)/m2 que cubre cada bote

import math


print("Bienvenidos al calculo de pintura por metros cuadrados ")

alto = int(input("Introduzca la altura de la pared en metros: "))
ancho = int(input("Introduzca el ancho de la pared en metros: "))
metros_por_bote = int(input("Introduzca los metros que cubre un bote de pintura: "))

def cantidad_botes_por_pared(alto,ancho,metros_por_bote):
    valor = (alto * ancho) / metros_por_bote
    numero_botes =  math.ceil(valor)
    return numero_botes


botes = cantidad_botes_por_pared(alto,ancho,metros_por_bote)
print(f"El total de botes de pinturas a comprar son {botes}")
