# Ejercicio

"""
Dado el fichero excel que os adjunto en varios formatos 
Copiar los datos al portapapeles
Crear un  dataframe "datos" con esos datos copiados
Mostrar por pantalla, todos datos del dataframe
Mostrar todos los nombres de columnas del dataframe
Mostrar la primera fila del dataframe
Mostrar la primera columna del  dataframe
Mostrar todos las filas pero solo las columnas "Continente" y "Poblacion"
Mostrar las primeras 3 filas del dataframe
Mostrar las 2 ultimas filas del dataframe

"""
import pandas as pd

datos = pd.read_clipboard() # Obtener valores los valores que son copiados en el sistema

print(datos)

print(datos.columns)

print(datos["Superficie"])

print(datos.loc[0])

print(datos.loc[ 0:3, ["Continente", "Población"] ])

print(datos.head(3))
print(datos.tail(3))
