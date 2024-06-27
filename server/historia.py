# Estructura para las historias

class Historia:
    def __init__(self, idhistoria, titulo, descripcion):
        self._id = idhistoria
        self._titulo = titulo
        self._descripcion = descripcion
        self._ramas = []

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def ramas(self):
        return list(self._ramas)

    def agregar_rama(self, historia):
        self._ramas.append(historia)

    def buscar_rama_nombre(self, nombre):
        for historia in self._ramas:
            if historia.titulo == nombre:
                return historia
        return None

    def buscar_rama_id(self, idrama):
        for historia in self._ramas:
            if historia.id == idrama:
                return historia
        return None

    def __str__(self):
        return f"{self.descripcion}"
