# Juego de piedra, papel o tijera

# El usuario elije también su opción 
# Ordenador elige una opción aleatoria

# Resultado 
# La tijera gana al papel
# El papel le gana a la piedra
# La piedra le gana a la tijera

import random

print("Bienvenidos al juego")
valor_usuario = int(input("Que opción quieres? Escribe '0' para piedra, '1' para papel y '2' para tijera: "))

valor_ordenador = random.randint(0,2)

print("Usuario = " + str(valor_usuario))
print(f"Ordenador = {valor_ordenador}")

if (valor_usuario == 0 and valor_ordenador == 2):
    print("Ha ganado el usuario")
elif (valor_usuario > valor_ordenador):
    print("Ha ganado el usuario")
elif (valor_usuario == valor_ordenador):
    print("Han quedado empatados")
else:
    print("Ha ganado el ordenador")

