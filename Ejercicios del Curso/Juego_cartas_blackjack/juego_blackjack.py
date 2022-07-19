#=========================
# Juego Blackjack
#=========================
"""
- Sumar tu cartas para que sean lo maximo posible sin pasarse de 2
- Si te pasas de 21, pierdes
- Las cartas j,q,k valen 10 puntos
- La carta '1' (as) puede valer 1 o 11 puntos(puedes elegir el que mas te convenga en cada caso),
- El cupier te da un carta levantada( se puede ver el valor) y el se coge 2 cargas (levanta 1 y la otra 
queda cubierta). Despues te da un asegunda carta levantada(se ve el valor)
- Es decir tu tienes 2 cartas levantadas( se ve el valor) y el cupier tiene 1 carta levantada y otra 
tapada (no se ve el valor)
- Luego te pregunta si quieres mas cartas. Si le dices que 'si', entonces elrupier te da otra carta 
descubierta, y te vuelve a preguntar si quieres otra mas cartas. Es decir te sigue dando cartas hasta que le dices 
que 'no' (no quieres mas cartas) o hasta que te has pasado de 21 y ya has perdido.
- Cuando ya no quieres mas  cartas, entonces el crupier levanta la carta que tenia tapada. Si la suma de sus cartas 
es menor que 17 (es decir 16 o menos) tendrá la obligación de coger una tercera carta. Si con esta carta ya suma 17 
o mas, entonces tendra que coger mas carts para intentar ganarte  o empatarte (es decir, que 
sus cartas suman un numero igual o mas grande que la suma de tus cartas)
- Ganas si la suma de tus cartas  es un valor  menor o igual a 21, y ademas la suma de tus cartas es mayor 
que la suma de las cartas del crupier (si tampoco se ha pasado de 21)
- Si el crupier se pasa de 21 , tu ganas.
- Si tu te pasas de 21, el crupier gana.
- Si la suma de tus cartas es igual a la suma de las cartas del crupier, entonces hay empatarte
- Recuerda que la carta con el numero '1' o 'as', puede valer '1' u  '11' (puedes elegir el valor que mas te convenga)
cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

""" 
import random
import replit


def generar_carta():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta = random.choice(cartas)
    return carta

def calcular_suma(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def mostrar_ganador(marcador_usuario,marcador_ordenador):
    if marcador_usuario == marcador_ordenador:
        # return "Empate"
        texto = " Empate "
    elif marcador_ordenador == 0:
        texto = "Has perdido, El ordenador tiene 21 - BlackJack"
    elif marcador_usuario == 0:
        texto = "Has Ganado!!! El ordenador ha perdido - Tienes 21 BlackJack"
    elif marcador_usuario > 21:
        texto = "Has perdido, la suma de tus cartas es mayor a 21"
    elif marcador_ordenador > 21:
        texto = "Has ganado!!!! La suma de las cartas del ordenador es mayor de 21"
    elif marcador_usuario > marcador_ordenador:
        texto = "Has ganado!!!"
    else:
        texto = "Has perdido"
    return texto

def jugar():
    print("Estamos jugando ...")

    cartas_usuario = []
    cartas_ordenador = []
    finalizado = False
    for valor in range(2):
        carta = generar_carta()
        cartas_usuario.append(carta)
        carta_ordenador = generar_carta()
        cartas_ordenador.append(carta_ordenador)
    while not finalizado:
        marcador_usuario = calcular_suma(cartas_usuario)
        marcador_ordenador = calcular_suma(cartas_ordenador)

        print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario} ")
        print(f"Cartas del ordenador = {cartas_ordenador[0]} ")

        if marcador_usuario == 0 or marcador_ordenador == 0 or marcador_usuario > 21:
            finalizado = True
        else:
            mas_cartas = input("Quieres mas cartas?. Escribe 'si' o 'no' " )
            if mas_cartas == 'si':
                carta = generar_carta()
                cartas_usuario.append(carta)
            else:
                finalizado = True
    while marcador_ordenador != 0 and marcador_ordenador < 17:
        carta_ordenador = generar_carta()
        cartas_ordenador.append(carta_ordenador)
        marcador_ordenador = calcular_suma(cartas_ordenador)

    print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
    print(f"Cartas del ordenador = {cartas_ordenador[0]}, marcador = {marcador_ordenador}")

    texto = mostrar_ganador(marcador_usuario, marcador_ordenador)
    print("texto")         

# Principio del programa
while input("Quieres jugar al BlackJack? Escribe 'si' o 'no' : ") == 'si':
    replit.clear()
    jugar()



# mi_carta = generar_carta()
# print(mi_carta)
mis_cartas = [10,11]
suma=calcular_suma(mis_cartas)
print(suma)
