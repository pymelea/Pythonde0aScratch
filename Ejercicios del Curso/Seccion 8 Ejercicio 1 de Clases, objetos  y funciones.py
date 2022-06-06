'''
Crear una clase "Coche" que tenga otros atributos;
marca, color, combustible y cilindrada

Crear la funcion __init__ que asigne los parametros de la clase a los atributos de la clase

Crear otra funcion "mostrar_características" que mediante print muestre por pantalla
las caracteristicas ( o atributos) que tiene el coche

Crear un objeto "coche1" de la clase "Coche" con los atributos "Opel", "rojo", "gasolina", "1.6"

Ejecute la funcion "mostrar_caracteristicas" del objeto "coche1"
'''

class Coche:

    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada= cilindrada

    def mostrar_caracteristicas(self,):
        print("Este coche es de la marcha {}, de color {}, con combustible de {} y con {} cilindros".format(self.marca, self.color, self.combustible, self.cilindrada ))

coche1 = Coche("Opel","rojo","gasolina","1.6")
coche1.mostrar_caracteristicas()