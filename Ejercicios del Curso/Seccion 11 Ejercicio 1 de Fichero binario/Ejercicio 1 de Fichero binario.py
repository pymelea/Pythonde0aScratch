'''
Crear el diccionario "frutas"
frutas = {"manzana":"apple", "naranja":"orange", "plátano":"banana", "limón":"lemon"}

Grabar esta estructura en un fichero binario "fichero.pckl"
Ya que en un fichero de texto, solo se guardan caracteres, pero no se pueden guardar estas estructuras

Recuperar esta estructura de datos del fichero "fichero.pckl"
Verificar que sigue siendo un diccionario, ejecutando el método .values()

'''
import pickle

frutas = {"manzana": "apple", "naranja": "orange",
          "plátano": "banana", "limón": "lemon"}
frutas.values()

fichero = open("fichero.pckl", "wb")
pickle.dump(frutas, fichero)

fichero.close()

fichero2 = open("fichero.pckl", "rb")
datos = pickle.load(fichero2)

print(datos)
datos.values()
