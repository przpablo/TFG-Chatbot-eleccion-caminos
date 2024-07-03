

class Sesion:
    def __init__(self, telefono, historial_actual, historias):
        self._telefono = telefono
        self._historial_actual = historial_actual
        self._historias = historias

    @property
    def telefono(self):
        return self._telefono

    @property
    def historia_actual(self):
        return self._historial_actual

    @property
    def historias(self):
        return list(self._historias)

    @historia_actual.setter
    def historia_actual(self, idhistoria):
        if idhistoria < 1000:
            raise ValueError(f"El ID de la historia {idhistoria} no es válido. Debe ser mayor o igual a 1000.")
        elif self.buscar_historia_por_id(idhistoria) is None:
            raise ValueError(f"El ID de la historia {idhistoria} no es valido. La historia no existe.")
        #elif self.buscar_historia_por_id(self._historial_actual).buscar_rama_id(idhistoria) is None:
        #    raise ValueError(f"El ID de la historia {idhistoria} no es valido. La historia no es rama.")
        else:
            self._historial_actual = idhistoria

    def buscar_historia_por_id(self, id_historia):
        for historia in self._historias:
            resultado = historia.buscar_historia_por_id(id_historia)
            if resultado is not None:
                return resultado
        return resultado
