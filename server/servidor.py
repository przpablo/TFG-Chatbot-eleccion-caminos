# Clase donde guardo la Historia y las Sesiones

from server.historia import Historia
# from sesion import Sesion


def crear_historia_principal():
    historia_inicio = Historia(1001, "inicio", "Despiertas en una playa desierta. "
                                               "El sol está alto en el cielo y el sonido de las olas es relajante. "
                                               "A lo lejos, divisas una densa <b>selva</b> y una oscura <b>cueva</b>."
                                               " ¿Qué camino decides tomar?")

    historia_selva = Historia(1002, "selva", "Te adentras en la selva y pronto el calor y la humedad se hacen intensos."
                                             " Mientras avanzas, escuchas ruidos entre los árboles. "
                                             "Un mono llamado Sam se te acerca, aparentemente amigable. "
                                             "Sam te pregunta hacia dónde te diriges: "
                                             "¿quieres seguir hacia el <b>rio</b> que se escucha a lo lejos, explorar "
                                             "un <b>camino</b> que parece peligroso, o intentar subir a un <b>árbol</b>"
                                             " alto para tener una mejor vista del área?")

    historia_cueva = Historia(1003, "cueva", "Ingresas a la cueva, el aire es fresco pero denso. La oscuridad es "
                                             "abrumadora, pero logras distinguir dos rutas posibles: un <b>tunel</b>"
                                             " que se adentra más en la cueva o una <b>salida</b> levemente iluminada"
                                             " a lo lejos. Sin embargo, también percibes un murmullo de agua en alguna"
                                             " parte, ¿te atreverías a seguir el <b>sonido</b> de ese murmullo?")

    historia_inicio.agregar_rama(historia_selva)
    historia_inicio.agregar_rama(historia_cueva)

    historia_rio = Historia(1004, "rio", "Llegas al río. El agua es cristalina, pero el río parece profundo y rápido. "
                                         "Puedes intentar <b>nadar</b> hasta la otra orilla, seguir caminando junto "
                                         "al <b>río</b> en busca de un puente, o explorar un pequeño <b>bote</b> "
                                         "abandonado que ves cerca de la orilla.")

    historia_sendero = Historia(1005, "sendero", "Decides seguir el sendero peligroso. La vegetación es densa y el"
                                                 " camino se vuelve cada vez más estrecho. Al final del sendero, "
                                                 "encuentras una <b>casa</b> abandonada, un <b>acantilado</b> "
                                                 "con una vista impresionante del mar, y una <b>cueva</b> que parece "
                                                 "no haber sido explorada en años.")

    historia_arbol = Historia(1008, "árbol", "Subes al árbol con dificultad, pero la vista desde la cima es "
                                             "impresionante. Desde allí, puedes ver un <b>claro</b> en la selva que"
                                             " parece seguro, una <b>montaña</b> en la distancia que podría ofrecer "
                                             "refugio, o puedes intentar observar más <b>animales</b> en la selva.")

    historia_selva.agregar_rama(historia_rio)
    historia_selva.agregar_rama(historia_sendero)
    historia_selva.agregar_rama(historia_arbol)

    historia_tunel = Historia(1006, "tunel", "Decides adentrarte en el túnel. La oscuridad es total y solo escuchas "
                                             "el eco de tus propios pasos. En el camino, encuentras un cofre antiguo "
                                             "que puedes intentar <b>abrir</b>, pero también sientes una corriente de "
                                             "aire que podría indicar otra <b>salida</b>. También puedes decidir "
                                             "<b>explorar</b> más profundamente el túnel, aunque no sabes qué podrías "
                                             "encontrar.")

    historia_salida = Historia(1007, "salida", "Optas por seguir hacia la salida iluminada. A medida que te acercas,"
                                               " la luz se vuelve más brillante hasta que te encuentras en una cámara "
                                               "natural iluminada por una abertura en el techo de la cueva. En esta "
                                               "cámara, puedes descansar en un <b>oasis</b> natural, explorar un "
                                               "<b>pasaje</b> oculto que ves a un lado, o salir hacia el "
                                               "<b>exterior</b> y continuar tu viaje.")

    historia_sonido = Historia(1009, "sonido", "Sigues el murmullo del agua y descubres un pequeño arroyo subterráneo. "
                                               "El agua parece potable, pero también puedes intentar seguir el arroyo"
                                               " más allá. Este camino te lleva a una bifurcación: una <b>escalera</b> "
                                               "de piedra que sube y un <b>camino</b> que sigue el curso del arroyo.")

    historia_cueva.agregar_rama(historia_tunel)
    historia_cueva.agregar_rama(historia_salida)
    historia_cueva.agregar_rama(historia_sonido)

    return historia_inicio


class Servidor:
    def __init__(self):
        self._historia_actual = crear_historia_principal()
        self._sesiones = {}

    def historia_actual(self):
        return self._historia_actual

    def sesiones(self):
        return self._sesiones

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
