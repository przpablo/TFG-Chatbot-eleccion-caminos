# Clase donde guardo la Historia y las Sesiones

from server.historia import Historia
# from sesion import Sesion


def crear_historia_principal():
    historia_inicio = Historia(1001, "inicio", "Despiertas en una playa desierta. "
                                               "Puedes ir a la selva o a la cueva.")

    historia_selva = Historia(1002, "selva", "Estás en la selva y te encuentras"
                                             "con el mono Sam, te pregunta que a donde os dirigís "
                                             "ahora, si al río o a un sendero un tanto peligroso.")
    historia_cueva = Historia(1003, "cueva", "Estás en una cueva oscura. Hay un túnel y una salida.")

    historia_inicio.agregar_rama(historia_selva)
    historia_inicio.agregar_rama(historia_cueva)

    historia_rio = Historia(1004, "río", "Llegaste al río. Puedes nadar o seguir caminando.")
    historia_sendero = Historia(1005, "sendero", "Sigues el sendero y encuentras una casa abandonada.")

    historia_selva.agregar_rama(historia_rio)
    historia_selva.agregar_rama(historia_sendero)

    historia_tunel = Historia(1006, "túnel", "Exploras el túnel y encuentras un tesoro.")
    historia_salida = Historia(1007, "salida", "Sales de la cueva y ves una luz brillante.")

    historia_cueva.agregar_rama(historia_tunel)
    historia_cueva.agregar_rama(historia_salida)

    return historia_inicio


class Servidor:
    def __init__(self):
        self._historia_actual = crear_historia_principal()
        self._sesiones = []

    def historia_actual(self):
        return self._historia_actual

    def sesiones(self):
        return list(self._sesiones)

    def obtener_situacion(self):
        return {
            "descripcion": self._historia_actual.descripcion,
            "opciones": [ramas.titulo for ramas in self._historia_actual.ramas]
        }

    def procesar_opcion(self, rama):
        if self._historia_actual.buscar_rama_id(rama):
            self._historia_actual = self._historia_actual.buscar_rama_id(rama)
            return self.obtener_situacion()
        return None
