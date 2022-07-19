''''
Subasta para calcular la apuesta mas alta

Flujo de trabajo:
    - Mensaje de bienvenida al programa de subasta
    - Preguntar por el nombre del primer apostante
    - Preguntar por el precio de su apuesta
    - Añadir el nombre (clave) y su apuesta (valor) a un diccionario de apuestas
    - Borrar la pantalla
    - Preguntar: si hay mas personas que quieren hacer su apuesta (si, no) (bucle hasta respuesta == no)
        Si respuesta = si
            - Preguntar nombre de la otra persona
            - Preguntar por su apuesta
            - Añadir el número (clave)  y su apuesta (valor) al diccionario de apuestas creado al principio
            - Borra la pantalla
        Si respuesta == no
            - Mostrar la apuesta ganadora de la subasta (apuesta con el precio más alto)
            - Fin de programa

'''
# from replit import clear
import os

def calcular_ganador(apuestas):
    apuesta_maxima = 0 
    ganador = ""
    for clave in apuestas:
        precio_apuesta = apuestas[clave]
        if precio_apuesta > apuesta_maxima:
            apuesta_maxima = precio_apuesta
            ganador = clave
    print(f"El gandador es {ganador} con un precio de {apuesta_maxima}")


print("Bienvenidos a la subasta que tendremos hoy")
apuestas = {}

mas_apuestas = True
while mas_apuestas:
    nombre = input("Cual es nombre del apostante?: ")
    precio = float(input("¿Cual es el precio de su apuesta?: "))

    apuestas[nombre] = precio

    pregunta = input("¿Hay mas personas que quieran hacer mas apuestas? Escribe 'si' o 'no': ")
    if pregunta == ' si':
        os.system('clear')
        # clear()
    elif pregunta == 'no':
        mas_apuestas =   False

# clear()
os.system('clear')
calcular_ganador(apuestas)
