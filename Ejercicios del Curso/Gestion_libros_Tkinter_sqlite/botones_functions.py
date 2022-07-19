import sqlite3

# Funcion para conectar la base de datos de libros
def conectar():
    conexion = sqlite3.connect("libro.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, year INTEGER, isbn INTEGER)")
    conexion.commit()
    conexion.close()


def insertar(titulo,autor,year,isbn):
    """Funcion para insertar los datos a la base de datos.

    Args:
        titulo:
        autor:
        year:
        isbn:
    """
    conexion = sqlite3.connect("libro.db")
    cursor = conexion.cursor()
    cursor.execute(" INSERT INTO libros VALUES (NULL,?,?,?,?)",(titulo,autor,year,isbn))
    conexion.commit()
    conexion.close()

def visualizar():
    conexion = sqlite3.connect("libro.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def buscar(titulo,autor,year,isbn):
    conexion = sqlite3.connect("libro.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR isbn=?",(titulo,autor,year,isbn))
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def borrar(id):
    conexion = sqlite3.connect("libro.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

def actualizar(titulo,autor,year,isbn,id):
    """actualizar.

    Args:
        titulo:
        autor:
        year:
        isbn:
        id:
    """
    conexion = sqlite3.connect("libro.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?,autor=?, year=?, isbn=? WHERE id=?",(titulo,autor,year,isbn,id))
    conexion.commit()
    conexion.close()



# Pruebas
conectar()
# insertar("titulo1","Autor1", 2007, 1244887)
resultados = visualizar()
for resultado in resultados:
    print(resultado)

