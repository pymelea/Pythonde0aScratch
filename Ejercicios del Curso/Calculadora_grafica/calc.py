from tkinter import *

ventana = Tk()
ventana.title("Calculadora en Python")
ventana.geometry("450x600")
ventana.resizable(False,False)
ventana.configure(background="gray")

# Funciones
operacion=""
resultado = StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,END)

def pulsar(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0,operacion)

def calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado = 'Error'
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0,resultado)


# Display de los resultados 
pantalla = Entry(ventana,font=("arial",20,"bold"), borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3,pady=10,padx=5)

# Boton de reiniciar operación
boton_reset = Button(ventana,text="AC",width=8,height=2,command=lambda:borrar())
boton_reset.grid(row=0,column=3,pady=10)

# Botones de la primera fila
ancho = 8
alto = 3

boton1 = Button(ventana,text="1",width=ancho,height=alto,command=lambda:pulsar(1))
boton1.grid(row=1,column=0,padx=5,pady=5)

boton2 = Button(ventana,text="2",width=ancho,height=alto,command=lambda:pulsar(2))
boton2.grid(row=1,column=1,padx=5,pady=5)


boton3 = Button(ventana,text="3",width=ancho,height=alto,command=lambda:pulsar(3))
boton3.grid(row=1,column=2,padx=5,pady=5)

boton4 = Button(ventana,text="4",width=ancho,height=alto,command=lambda:pulsar(4))
boton4.grid(row=1,column=3,padx=5,pady=5)

# Botones de la fila 2

boton5 = Button(ventana,text="5",width=ancho,height=alto,command=lambda:pulsar(5))
boton5.grid(row=2,column=0,padx=5,pady=5)

boton6 = Button(ventana,text="6",width=ancho,height=alto,command=lambda:pulsar(6))
boton6.grid(row=2,column=1,padx=5,pady=5)


boton7 = Button(ventana,text="7",width=ancho,height=alto,command=lambda:pulsar(7))
boton7.grid(row=2,column=2,padx=5,pady=5)

boton8 = Button(ventana,text="8",width=ancho,height=alto,command=lambda:pulsar(8))
boton8.grid(row=2,column=3,padx=5,pady=5)

# Botones de la fila 3

boton9 = Button(ventana,text="9",width=ancho,height=alto,command=lambda:pulsar(9))
boton9.grid(row=3,column=0,padx=5,pady=5)

boton0 = Button(ventana,text="0",width=ancho,height=alto,command=lambda:pulsar(0))
boton0.grid(row=3,column=1,padx=5,pady=5)


boton_punto = Button(ventana,text=".",width=ancho,height=alto,command=lambda:pulsar("."))
boton_punto.grid(row=3,column=2,padx=5,pady=5)

boton_suma = Button(ventana,text="+",width=ancho,height=alto,command=lambda:pulsar("+"))
boton_suma.grid(row=3,column=3,padx=5,pady=5)

# Botones de la fila 4

boton_menos = Button(ventana,text="-",width=ancho,height=alto,command=lambda:pulsar("-"))
boton_menos.grid(row=4,column=0,padx=5,pady=5)

boton_multi = Button(ventana,text="*",width=ancho,height=alto,command=lambda:pulsar("*"))
boton_multi.grid(row=4,column=1,padx=5,pady=5)


boton_div = Button(ventana,text="/",width=ancho,height=alto,command=lambda:pulsar("/"))
boton_div.grid(row=4,column=2,padx=5,pady=5)

boton_igual = Button(ventana,text="=",width=ancho,height=alto,command=lambda:calcular())
boton_igual.grid(row=4,column=3,padx=5,pady=5)

ventana.mainloop()

