'''
Crear una variable "tupla" que sea una tupla de los siguientes nombres: Antonio, Pedro, María
Mostrar el valor de la variable "tupla"
Recoger un dato por teclado y almacenarlo en la variable "dato"
Si el valor  de "dato" está dentro de los valores de la variable "tupla", mostrar "SI"
Si el valor  de "dato" no está dentro de los valores de la variable "tupla", mostrar "NO"
'''

nombres = ("Antonio", "Pedro", "María")
print(nombres)
dato = input("Introduce un nombre: ")
if dato in nombres:
    print("SI")
else:
    print("NO")