# Ejercicio

"""
Leer el fichero adjunto "poblacion.xlsx" y cargar los datos en un dataframe
Com esos datos, visualizar cual es la ciudad mas poblada en America

Leer el fichero adjunto "poblacion.csv" y cargar los datos en un dataframe
Con esos datos, visualizar cual es la ciudad mas poblada en Africa

"""

import pandas as pd
#import numpy as np

fichero_excel = pd.ExcelFile('/home/lily/Projects/De 0 a experto en Python/10_proyectos /Ejercicios del Curso/Seccion_20_Modulo_pandas/poblacion.xlsx')

fichero_csv = pd.read_csv('/home/lily/Projects/De 0 a experto en Python/10_proyectos /Ejercicios del Curso/Seccion_20_Modulo_pandas/poblacion2.csv', sep=';')
# fichero_excel = pd.ExcelFile('/home/lily/Projects/De 0 a experto en Python/10_proyectos /Ejercicios del Curso/Seccion_20_Modulo_pandas/poblacion.xlsx')

dataframe_excel = fichero_excel.parse('Hoja 1')
print(dataframe_excel)

#dataframe_excel = dataframe_excel.loc[6]

#print(dataframe_excel)
dataframe = dataframe_excel['Ciudad más poblada'][3]
print(dataframe)

print(fichero_csv)

print(fichero_csv['Ciudad más poblada'][1])
