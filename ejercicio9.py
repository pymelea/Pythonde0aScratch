'''
Crear una variable "numeros" con la lista de los numeros del uno al 10 ( ambs incluidos)
Mostarr el valor de la variable "numeros"
Recoger un dato del teclado y almacenalo en la variable "dato"
Convierte "dato" en numerico y almacenalo en la variable "numero"
Si el valor de "numero" está en la lista de números mostrar el mensaje "SI"
Si el número introducido no está en la lista de números mostrar el mensaje "NO"
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

print(numeros)

dato = int(input("Introduce un numero: "))

if dato in numeros:
    print("El número SI está en la lista")
    
else:
    print("El número NO está en la lista")
