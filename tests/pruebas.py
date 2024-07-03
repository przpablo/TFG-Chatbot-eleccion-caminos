

import unittest

from server.historia import Historia
from server.sesion import Sesion


class TestHistoria(unittest.TestCase):
    def setUp(self):
        self.historia = Historia(1000, "Inicio", "Hola")

        self.rama01 = Historia(1001, "Rama1", "Opcion 1 de la historia principal")
        self.rama02 = Historia(1002, "Rama2", "Opcion 2 de la historia principal")
        self.historia.agregar_rama(self.rama01)
        self.historia.agregar_rama(self.rama02)

        self.rama11 = Historia(1003, "Rama3", "Opcion 1 de la rama1")
        self.rama22 = Historia(1004, "Rama4", "Opcion 2 de la rama2")
        self.rama01.agregar_rama(self.rama11)
        self.rama02.agregar_rama(self.rama22)

        self.historias = [self.historia, self.rama01, self.rama02, self.rama11, self.rama22]

        self.sesion1 = Sesion(123454545, self.historia.id, self.historias)
        self.sesion2 = Sesion(123646464, self.historia.id, self.historias)

    def test_creacion_historia(self):
        self.assertEqual(1000, self.historia.id)
        self.assertEqual("Inicio", self.historia.titulo)
        self.assertEqual(2, len(self.historia.ramas))

    def test_creacion_sesion(self):
        self.assertEqual(123454545, self.sesion1.telefono)
        self.assertEqual(1000, self.sesion1.historia_actual)

    def test_cambio_historia(self):
        self.sesion1.historia_actual = self.rama01.id
        self.sesion2.historia_actual = self.rama02.id
        self.assertEqual(1001, self.sesion1.historia_actual)
        self.assertEqual(1002, self.sesion2.historia_actual)

    def test_cambio_historia2(self):
        self.sesion1.historia_actual = self.rama11.id
        self.sesion2.historia_actual = self.rama22.id
        self.assertEqual(1003, self.sesion1.historia_actual)
        self.assertEqual(1004, self.sesion2.historia_actual)

    def test_cambio_historia3(self):
        self.sesion1.historia_actual = 1099
        self.assertEqual(1099, self.sesion1.historia_actual)

    def test_cambio_historia4(self):
        self.sesion2.historia_actual = -1005
        self.assertEqual(-1005, self.sesion2.historia_actual)


class TestConArchivos(unittest.TestCase):
    def setUp(self):
        self.historia = Historia(2000, "Inicio", "Hola")

        self.rama01 = Historia(2001, "Rama1", "Opcion 1 de la historia principal")
        self.rama02 = Historia(2002, "Rama2", "Opcion 2 de la historia principal")
        self.historia.agregar_rama(self.rama01)
        self.historia.agregar_rama(self.rama02)

        self.rama11 = Historia(2003, "Rama3", "Opcion 1 de la rama1")
        self.rama22 = Historia(2004, "Rama4", "Opcion 2 de la rama2")
        self.rama01.agregar_rama(self.rama11)
        self.rama02.agregar_rama(self.rama22)

        self.historias = [self.historia, self.rama01, self.rama02, self.rama11, self.rama22]

        self.sesiones = {
            123454545: Sesion(123454545, self.historia.id, self.historias),
            123646464: Sesion(123646464, self.historia.id, self.historias)
        }

    def leer_y_procesar_elecciones(self, archivo):
        with open(archivo, 'r') as file:
            for linea in file:
                if linea.startswith("#"):
                    continue
                telefono, opcion = map(int, linea.strip().split(","))
                sesion = self.sesiones.get(telefono)
                if sesion:
                    try:
                        sesion.historia_actual = opcion
                        print(f"Teléfono {telefono}: Cambio exitoso a la historia {sesion.historia_actual}")
                    except ValueError as e:
                        print(f"Teléfono {telefono}: {e}")

    def test_elecciones_desde_archivo(self):
        self.leer_y_procesar_elecciones('sesiones.txt')


if __name__ == "__main__":
    unittest.main()
