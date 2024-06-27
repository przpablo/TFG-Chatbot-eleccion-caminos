# Estructura para las historias

class Historia():
    def __init__(self, titulo, descripcion):
        self._titulo = titulo
        self._descripcion = descripcion
        self._opciones = []

    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def opciones(self):
        return list(self._opciones)

    def agregar_opcion(self, historia):
        self._opciones.append(historia)

    def buscar_opcion(self, nombre):
        for historia in self._opciones:
            if historia.titulo == nombre:
                return historia
        return None


    def __str__(self):
        return f"{self.descripcion}"
