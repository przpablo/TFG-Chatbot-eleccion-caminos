from historia import Historia

class Server:
    def __init__(self):
        self._historia_actual = self.crear_historia_principal()
        self._sesiones = []

    def historia_actual(self):
        self._historia_actual

    def sesiones(self):
        return self._sesiones

    def crear_historia_principal(self):
        historia_inicio = Historia("Inicio", "Despiertas en una playa desierta. Puedes ir a la selva o a la cueva.")

        historia_selva = Historia("selva", "Estás en la selva. Hay un río y un sendero.")
        historia_cueva = Historia("cueva", "Estás en una cueva oscura. Hay un túnel y una salida.")

        historia_inicio.agregar_opcion(historia_selva)
        historia_inicio.agregar_opcion(historia_cueva)

        historia_rio = Historia("río", "Llegaste al río. Puedes nadar o seguir caminando.")
        historia_sendero = Historia("sendero", "Sigues el sendero y encuentras una casa abandonada.")

        historia_selva.agregar_opcion(historia_rio)
        historia_selva.agregar_opcion(historia_sendero)

        historia_tunel = Historia("túnel", "Exploras el túnel y encuentras un tesoro.")
        historia_salida = Historia("salida", "Sales de la cueva y ves una luz brillante.")

        historia_cueva.agregar_opcion(historia_tunel)
        historia_cueva.agregar_opcion(historia_salida)

        return historia_inicio

    def obtener_situacion(self):
        return {
            "descripcion": self._historia_actual.descripcion,
            "opciones": [opcion.titulo for opcion in self.historia_actual.opciones]
        }

    def procesar_opcion(self, opcion):
        if self._historia_actual.buscar_opcion(opcion):
            self._historia_actual = self._historia_actual.buscar_opcion(opcion)
            return self.obtener_situacion()
        return None
