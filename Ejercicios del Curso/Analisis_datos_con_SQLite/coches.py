from sqlite3 import Error
import sqlite3
import sys
from zipfile import ZipFile
import pandas as pd
from os import remove 

basededatos = 'coches.db'

def precio_medio_por_marca(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT marca, AVG(precio) FROM coches GROUP BY marca")
    datos = cursor.fetchall()
    return datos

def marca_coche_mas_barato(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT marca, modelo, MIN(precio) FROM coches")
    mas_barato = cursor.fetchall()
    # dato = mas_barato[0][0]
    return mas_barato

def precio_total_coche(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT SUM(precio) FROM coches')
    dato = cursor.fetchall()
    precio = dato[0][0]
    return precio
    

def numero_coches_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM coches')
    dato = cursor.fetchall()
    numero = dato[0][0]
    return numero

def consultar_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM coches LIMIT 20')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def borrar_datos():
    try:
        remove(basededatos)
    except FileNotFoundError:
        pass

def insertar_tabla_coche(conexion,coche):
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO coches(marca,modelo,combustible,transmision,estado,matriculacion,kilometraje,potencia,precio) VALUES (?,?,?,?,?,?,?,?,?)', coche)
    conexion.commit()

def grabar_coches(conexion,datos):
    for fila in datos.itertuples():
        marca = fila[1]
        modelo = fila[2]
        combustible = fila[3]
        transmision = fila[4]
        estado = fila[5]
        matriculacion = fila[6]
        kilometraje = fila[7]
        potencia = fila[8]
        precio = fila[9]

        coche = (marca,modelo,combustible,transmision,estado,matriculacion,kilometraje,potencia,precio)
        insertar_tabla_coche(conexion,coche)


def crear_tabla_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE coches(marca text,modelo text, combustible text, transmision text, estado text, matriculacion text, kilometraje integer, potencia real, precio real)')
    conexion.commit()


def crear_conexion_db():
    try:
        conexion = sqlite3.connect(basededatos)
        return conexion
    except Error:
        print(Error)

def leer_datos(nombre):
    datos = pd.read_csv(nombre, sep=';')
    return datos

def descomprimir_fichero(nombre):
    with ZipFile(nombre,'r') as zip:
        zip.extractall()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error. Número de parametros incorrecto, Puede faltar el nombre del archivo")
    else:
        nombre_fichero = sys.argv[1]
        print(nombre_fichero)

        borrar_datos()

        descomprimir_fichero(nombre_fichero)

        datos = leer_datos(nombre_fichero)
        print(datos)

        conexion = crear_conexion_db()

        crear_tabla_coches(conexion)

        grabar_coches(conexion, datos)

        print("\n Consultamos los datos de la tabla.")
        consultar_coches(conexion)

        dato = numero_coches_tabla(conexion)
        print(" \n El número de coches es de {}".format(dato))

        precio = precio_total_coche(conexion)
        dinero = '{:,}'.format(precio).replace(',','.')
        print("\n El precio total delos coches es de {}".format(dinero))

        datos = marca_coche_mas_barato(conexion)
        marca = datos[0][0]
        modelo = datos[0][1]
        precio = datos[0][2]
        print("\n Coche más barato, Marca = {}, Modelo = {}, Precio = {}".format(marca,modelo,precio))

        print("\n Precio medio por marca de coches \n")
        datos = precio_medio_por_marca(conexion)
        for dato in datos:
            marca = datos[0]
            precio = datos[1]
            print(marca, precio)

