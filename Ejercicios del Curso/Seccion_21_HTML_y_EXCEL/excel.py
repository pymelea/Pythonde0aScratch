# Trabajar con ficheros EXCEL
# pip install openpyxl
import pandas as pd

fichero_excel = pd.ExcelFile('/home/lily/Projects/De 0 a experto en Python/10_proyectos /Ejercicios del Curso/Seccion_20_Modulo_pandas/poblacion.xlsx')

dataframe = fichero_excel.parse('Hoja 1')

print(dataframe)
