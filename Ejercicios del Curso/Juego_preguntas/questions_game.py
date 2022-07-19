# Juego de preguntas 

print("Bienvenidos al juego de preguntas")
respuesta_orientacion = input("¿Quieres is a la izquierda o a la derecha?, Escribe 'izquierda' o 'derecha' ").lower()
if respuesta_orientacion == 'izquierda':
    print(" Respuesta erronea, Te has caido en un agujero y has perdido. Puedes volver a intentarlo")
else:
    respuesta_cruzar = input("Tienes que cruzar a una isla. Quieres ir nadando o quieres esperar a un barco para cruzar. Escribe 'nadar' o 'esperar'").lower()
    if respuesta_cruzar == 'nadar':
        print("Respuesta erronea. Habia tiburones. Has perdido puedes volver a intentarlo")
    else:
        respuesta_color = input(" Has llegado a una casa  que tiene 3 puertas. Una puesta de color azul, otra de color rojo y otra puerta de color verde. ¿Que puerta quieres abrir? Escribe 'azul', 'rojo' o 'verde' ")
        respuesta_color = respuesta_color.lower()
        if respuesta_color == 'rojo' or respuesta_color == 'azul':
            print("Respuesta erronea. Has perdido. Puedes volver a intentarlo")
        else:
            print("En hora buena ha ganado el juego !!!")

