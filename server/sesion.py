

class Sesion:
    def __init__(self, telefono, historial_actual):
        self._telefono = telefono
        self._historial_actual = historial_actual

    @property
    def telefono(self):
        return self._telefono

    @property
    def historia_actual(self):
        return self._historial_actual

    @historia_actual.setter
    def historia_actual(self, id_historia):
        self._historial_actual = id_historia