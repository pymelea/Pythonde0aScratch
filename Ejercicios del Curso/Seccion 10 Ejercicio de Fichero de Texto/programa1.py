# Inportando el modulo donde esta declarada la clase
import moduloficheros

nombre_fichero = "fichero.txt"

# Creando objeto fichero1 de tipo Fichero()
fichero1 = moduloficheros.Fichero(nombre_fichero)

# Grabando texto  en el fichero
texto = "Este es una prueba"
fichero1.grabar_fichero(texto)

#  Incluir texto  en el fichero
texto = "\nEsta es otra linea para agregar"
fichero1.incluir_fichero(texto)

# Leer texto  del fichero
texto_leido = fichero1.leer_fichero()
print(texto_leido)