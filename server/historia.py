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
        if historia.id < 1000:
            raise ValueError(f"El ID de la historia {historia.id} no es válido. Debe ser mayor o igual a 1000.")
        else:
            self._ramas.append(historia)

    def buscar_historia_por_id(self, idhistoria, visitados=None):
        if visitados is None:
            visitados = set()

        if self.id == idhistoria:
            return self

        # Evitar un ciclo infinito
        if self.id in visitados:
            return None

        visitados.add(self.id)

        for rama in self.ramas:
            resultado = rama.buscar_historia_por_id(idhistoria, visitados)
            if resultado is not None:
                return resultado

        return None

    def buscar_rama_nombre(self, nombre):
        for historia in self._ramas:
            if historia.titulo.strip().lower() == nombre.strip().lower():
                return historia
        return None

    def buscar_rama_id(self, idrama):
        for historia in self._ramas:
            if historia.id == idrama:
                return historia
        return None

    def __str__(self):
        return f"{self.descripcion}"
