'''
Clase Fichero que incluye el constructor de la clase
y los metodos Leer_fichero, Grabar_fichero e Incluir_fichero.
El fichero es de tipo .txt
'''

class Fichero():

    def __init__(self, nombre):
        self.nombre = nombre

    def leer_fichero(self):
        fichero = open(self.nombre, "rt")
        contenido = fichero.read()
        return contenido
        # fichero.close()


    def grabar_fichero(self, texto):
        fichero = open("fichero.txt", "wt")
        fichero.write(texto)
        fichero.close()

    def incluir_fichero(self, texto):
        fichero = open("fichero.txt", "at")
        fichero.write(texto)
        fichero.close()
