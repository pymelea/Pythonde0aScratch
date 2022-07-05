# Ejemplo

# Crear una lista de 1000 valores aleatorios que sigan una distribución normal
# Crear un hostograma mediante matplotlib con la lista de valores
# Crear un diagrama de caja (donde se acumula el 50% de los valores) mediante seaborn


# Solución

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

lista_valores = np.random.randn(1000)
print(lista_valores)

histograma = plt.hist(lista_valores)

print(histograma)


diagrama_caja = sns.boxplot(lista_valores)
print(diagrama_caja)
