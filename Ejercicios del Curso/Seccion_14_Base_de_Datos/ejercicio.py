'''
Crear una base de datos "sqlite.db"
Crear una tabla "productos" con 3 campos
    id: Identificador  del producto de tipo numérico
    nombre: Nombre delproduct de tipo texto
    precio: Precio del porducto de tipo numérico

Insertar 3 productos en la tabla "productos"
    1. "Impresora", 300
    2. "Raton", 20
    3. "Ordenador", 600

Consultar los productos de la tabla "productos"
Cerrar la base de datos "sqlite.db"

'''

import sqlite3

conexion = sqlite3.connect("sqlite.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE PRODUCTO (id INTEGER, nombre TEXT, precio INTEGER) ")

# lista_productos = [(1, 'Impresora', 300), (2,'Raton', 20), (3,'Ordenador', 600)] 

# cursor.executemany("INSERT INTO PRODUCTO VALUES (?,?,?)", lista_productos)

cursor.execute("SELECT * FROM PRODUCTO")

productos = cursor.fetchall()

# conexion.commit()

for producto in productos:
    print(producto)

# conexion.close()
