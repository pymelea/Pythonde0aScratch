
# HTML con Python

import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.io.html.read_html(url)

print(dataframe)

dataframe_futbol = dataframe[0]
#print(dataframe_futbol)
#print(dataframe_futbol.loc[0])

#print(dict(dataframe_futbol.loc[0]))

#dataframe_futbol = dataframe_futbol.rename(columns=dict(dataframe_futbol.loc[0]))

#print(dataframe_futbol)

#Eliminar una fila 
#dataframe_futbol = dataframe_futbol.drop(0)
#print(dataframe_futbol)

dataframe_futbol = dataframe_futbol.drop('Notas', axis=1)
print(dataframe_futbol)
