# Ejercicio

# Crear 2 arrays con 9 numeros aleatorios entre los valores 0 y 100

# Cambiar el formato de los valores en una estrutura de 3 filas por 2 columnas

# Crear 2 dataframes con esos arrays

# Concatenar esos 2 dataframes


import pandas as pd
import numpy as np

array1 = np.random.randint(0,100,9)
array2 = np.random.randint(0,100,9).reshape(3,3)

array1.resize(3,3)

print(array1)
dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)

print(dataframe1, dataframe2)


dataframe_concatenacion = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframe_concatenacion)
