# Ejercicio 

# Vamos a filtrar datos en un DataFrame

# Crearemos una lista de 50 valores aleatorios enteros entre los valores 0 y 100
# Covertiremos esta lista en un DataFrame con 5 filas y 10 columnas
# Filtraremos los datos del DataFrame para visualizar solo los valores que sean mayores de 50

import pandas as pd
import numpy as np

lista_valores = np.random.randint(0,100,50) # Generando una lista de valores enteros aletorios  entre 0 y 100

print(lista_valores)

lista_valores.resize(5,10) # Convirtiendo las lista de valores a un DataFrame de 5 filas y 10 columnas

print(lista_valores)

dataframe = pd.DataFrame(lista_valores) # Convirtiendolo en dataframe

print(dataframe)

print(dataframe[dataframe>50]) # Filtrando los valores que sean mayores de 50 
