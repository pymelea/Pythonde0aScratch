'''
Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
crear una variable "longitud" que contiene la longitud de la "cadena"
Crear una variable "sttrlongitud" que tenga el valor de la "longitud " pero convertida a cadena de caracteres string
crear una variable "mayusculas" que contiene la variable "cadena" en máyusculas
crear una variable "resultado" que contiene la variable "mayusculas" con el texto "tiene longitud de "  y  "strlongitud"
'''

cadena = "Esto es un texto de ejemplo"

longitud = len(cadena)

strlongitud = str(longitud)

mayusculas = cadena.upper()

resultado = mayusculas + " tiene longitud de " + strlongitud

# print(longitud)

print(resultado)