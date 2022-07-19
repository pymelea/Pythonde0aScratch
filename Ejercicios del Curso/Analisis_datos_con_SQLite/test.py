import unittest
from coches import *

nombre_fichero = 'coches.csv'

class test_numero_coches_tabla(unittest.TestCase):

    def test(self):
        
        borrar_datos()

        datos = leer_datos(nombre_fichero)
        
        conexion = crear_conexion_db()

        crear_tabla_coches(conexion)

        grabar_coches(conexion,datos)

        dato = numero_coches_tabla(conexion)
        self.assertEqual(2780,dato)

class test_precio_total_coches(unittest.TestCase):
    def test_precio(self):

        borrar_datos()

        datos = leer_datos(nombre_fichero)

        conexion = crear_conexion_db()

        crear_tabla_coches(conexion)

        grabar_coches(conexion,datos)

        dato = precio_total_coche(conexion)
        dinero = '{:,}'.format(dato).replace(',','.')

        self.assertEqual('38,997,136.0', dinero)
        

if __name__ == "__main__":
    unittest.main()


