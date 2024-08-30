# Clase donde guardo la Historia y las Sesiones

from server.historia import Historia
# from sesion import Sesion


def crear_historia_principal():
    historia_inicio = Historia(1001, "inicio", "Este es el inicio de la Historia. Despiertas en una isla desierta "
                                               "después del aterrizaje forzoso del avión al que ibamos camino a Bali."
                                               " Sois una tripulación de 100 personas y tienes que tomar las decisiones"
                                               " podréis terminar salvados, ricos o muertos. "
                                               "El sol está alto en el cielo y el sonido de las olas es relajante. "
                                               "A lo lejos, divisas una densa <b>selva</b> y una oscura <b>cueva</b>."
                                               " ¿Qué camino decides tomar?")

    historia_selva = Historia(1002, "selva", "Te adentras en la selva y pronto el calor y la humedad se hacen intensos."
                                             " Mientras avanzas, escuchas ruidos entre los árboles. "
                                             "Un mono llamado Sam se te acerca, aparentemente amigable. "
                                             "Sam te pregunta hacia dónde te diriges: "
                                             "¿quieres seguir hacia el <b>rio</b> que se escucha a lo lejos, explorar "
                                             "un <b>camino</b> que parece peligroso, o intentar subir a un <b>arbol</b>"
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
                                         "al río en busca de un <b>puente</b>, o explorar un pequeño <b>bote</b> "
                                         "abandonado que ves cerca de la orilla.")

    historia_nadar = Historia(1010, "nadar", "NO! Intentas nadar pero la corriente es tan fuerte que te desplaza "
                                             "tanto que te caes por un acantilado y morís todos. Fin de la historia"
                                             " pulsa /inicio para reiniciar.")

    historia_puente = Historia(1011, "puente", "Tras un largo viaje de varias horas andando por la orilla del rio"
                                               " encontrais un <b>túnel</b> que no muestra mucha confianza pero es la"
                                               "única opción.")

    historia_bote = Historia(1012, "bote", "Tras ir rio abajo y salvaros de un acantilado gracias al bote"
                                           "llegáis al mar donde os avista un barco pesquero y os salva todos!"
                                           "Acabéis conseguido salvaros! Pulsa /inicio si quieres reiniciar la "
                                           "historia.")

    historia_rio.agregar_rama(historia_nadar)
    historia_rio.agregar_rama(historia_puente)
    historia_rio.agregar_rama(historia_bote)

    historia_sendero = Historia(1005, "sendero", "Decides seguir el sendero peligroso. La vegetación es densa y el"
                                                 " camino se vuelve cada vez más estrecho. Al final del sendero, "
                                                 "encuentras una <b>casa</b> abandonada donde "
                                                 "vive el mono Sam y sus amigos, un <b>acantilado</b> "
                                                 "con una vista impresionante del mar, y una <b>cueva</b> que parece "
                                                 "no haber sido explorada en años.")

    historia_casa = Historia(1013, "casa", "Llegas a la casa y está en perfecto estado, parece ser que es un refugio."
                                           " Hay un télefono! Estáis todos salvados, alertáis por telefono donde estais"
                                           " y os salvan. Pulsa /inicio si quieres reiniciar la "
                                           "historia.")

    historia_acantilado = Historia(1014, "acantilado", "Las vistas desde el acantilado son increibles pero no hay "
                                                       "muchas opciones para hacer ahí, asi que tienes que dar la "
                                                       "vuelta y volver al <b>sendero</b>.")

    historia_sendero.agregar_rama(historia_cueva)
    historia_sendero.agregar_rama(historia_casa)
    historia_sendero.agregar_rama(historia_acantilado)

    historia_arbol = Historia(1008, "arbol", "Subes al árbol con dificultad, pero la vista desde la cima es "
                                             "impresionante. Te haces una pequeña idea de la magnitud de la isla "
                                             "es inmensa. Desde allí, puedes ver un <b>oasis</b> en la selva que"
                                             " parece seguro, una <b>cueva</b> en la distancia que podría ofrecer "
                                             "refugio, o puedes intentar observar más animales en la selva en busqueda"
                                             "de algun <b>sonido</b>.")

    historia_oasis = Historia(1015, "oasis", "Vais hacia el oasis que visteis en el arbol. Llegáis a allí y no hay "
                                             "nada, por lo tanto decidís volver al /inicio.")

    historia_arbol.agregar_rama(historia_cueva)
    historia_arbol.agregar_rama(historia_oasis)

    historia_selva.agregar_rama(historia_rio)
    historia_selva.agregar_rama(historia_sendero)
    historia_selva.agregar_rama(historia_arbol)

    historia_tunel = Historia(1006, "tunel", "Decides adentrarte en el túnel. La oscuridad es total y solo escuchas "
                                             "el eco de tus propios pasos. En el camino, encuentras un <b>cofre</b> "
                                             "antiguo "
                                             "que puedes intentar abrir, pero también sientes una corriente de "
                                             "aire que podría indicar otra <b>salida</b>. También puedes decidir "
                                             "<b>explorar</b> más profundamente el túnel, aunque no sabes qué podrías "
                                             "encontrar.")

    historia_cofre = Historia(1016, "cofre", "Encontrais un cofre pirata de hace miles de años y esta lleno de oro! "
                                             "Hay oro suficiente para haceros ricos a toda la tripulacion. Podéis "
                                             "ir a la <b>salida</b> o volver a <b>explorar</b> todavia un poco mas "
                                             "el tunel.")
    historia_explorar = Historia(1017, "explorar", "NO! Seguís explorando el túnel y de repente se despeja todo y "
                                                   "ya no tenéis salida, estáis acabados! Pulsa /inicio para reiniciar"
                                                   " historia.")

    historia_cofre.agregar_rama(historia_explorar)

    historia_tunel.agregar_rama(historia_cofre)
    historia_tunel.agregar_rama(historia_explorar)

    historia_puente.agregar_rama(historia_tunel)

    historia_salida = Historia(1007, "salida", "Optas por seguir hacia la salida iluminada. A medida que te acercas,"
                                               " la luz se vuelve más brillante hasta que te encuentras en una cámara "
                                               "natural iluminada por una abertura en el techo de la cueva. En esta "
                                               "cámara, puedes descansar en un <b>oasis</b> natural, explorar un "
                                               "<b>pasaje</b> oculto que ves a un lado, o salir hacia el "
                                               "<b>rio</b> y continuar tu viaje.")

    historia_pasaje = Historia(1018, "pasaje", "Exploráis el pasaje a la salida de la cueva y veis que "
                                               "hay un <b>cofre</b>. Decidís abrirlo si o si, no hay otra opción.")

    historia_pasaje.agregar_rama(historia_cofre)

    historia_salida.agregar_rama(historia_rio)
    historia_salida.agregar_rama(historia_oasis)
    historia_salida.agregar_rama(historia_pasaje)

    historia_tunel.agregar_rama(historia_salida)
    historia_cofre.agregar_rama(historia_salida)

    historia_sonido = Historia(1009, "sonido", "Sigues el murmullo del agua y descubres un pequeño arroyo subterráneo. "
                                               "El agua parece potable, pero también puedes intentar seguir el arroyo"
                                               " más allá. Este camino te lleva a una bifurcación: una <b>escalera</b> "
                                               "de piedra que sube y un camino que sigue el curso del <b>rio</b>.")

    historia_escalera = Historia(1019, "escalera", "Subís las escaleras y llegáis a un <b>acantilado</b>, habeis subido"
                                                   " tanto que no os queda otra opción que seguir.")

    historia_escalera.agregar_rama(historia_acantilado)

    historia_sonido.agregar_rama(historia_rio)
    historia_sonido.agregar_rama(historia_escalera)

    historia_arbol.agregar_rama(historia_sonido)

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
