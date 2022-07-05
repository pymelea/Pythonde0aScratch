# Ejercicio 

# Crear un array con 100 números enteros aleatorios con valores comprendidos entre 0 y 500
# Crear un diagrama de caja para representar los valores aleatorios ganerados

import numpy as np
import seaborn as sns

lista_valores = np.random.randint(0,500,100)
print(lista_valores)

diagrama_caja = sns.boxplot(lista_valores)
print(diagrama_caja)


