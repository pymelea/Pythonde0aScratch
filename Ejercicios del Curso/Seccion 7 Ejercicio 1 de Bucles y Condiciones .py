'''
Crear un diccionario con los siguientes pares de valores
    manzana, apple
    naranja, orange
    platano, banana
    limon, lemon

Muestra la traduccion para la palabra "naranja"
Añade un elemento nuevo con "piña" y "pineapple".
Haz un bucle para mostrar todos los elementos del diccionario

'''

frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon" }
frutas["piña"] = "pineapple"

for key,value in frutas.items():
    print("{} en inglés es {}".format(key.upper(),value))


