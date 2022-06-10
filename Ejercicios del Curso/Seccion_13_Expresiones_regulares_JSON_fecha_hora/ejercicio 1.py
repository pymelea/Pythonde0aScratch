'''
Crear una funcion "buscar" que mediantes una expresion reguar indique si una palabra está en una frase

Probar la funcion "buscar" con estas frases
    texto = "Esto es una frase de pruebas para hacer busquedas"
    palabra_a_buscar = "frase"

En caso de encontrar la palabra en la frase, indicar en que posición empieza y en cual finaliza
'''

import re

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = "frase"


def buscar(texto, palabra_a_buscar):
    busqueda = re.search(palabra_a_buscar,texto)
    # print(busqueda)
    inicial = busqueda.start()
    final = busqueda.end()
    print("Empieza en la posición {} y finaliza en la posición {}".format(inicial,final))
    if (busqueda):
        print("Palabra {} encontrada".format(palabra_a_buscar))
    else:
        print("Palabra {} NO encontrada".format(palabra_a_buscar))
    return busqueda

buscar(texto,palabra_a_buscar)



