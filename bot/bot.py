import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from server.historia import Historia
from server.sesion import Sesion


class Server:
    def __init__(self):
        self._historia_actual = self.crear_historia_principal()
        self._sesiones = []

    def historia_actual(self):
        return self._historia_actual

    def sesiones(self):
        return list(self._sesiones)

    def crear_historia_principal(self):
        historia_inicio = Historia(1001, "Inicio", "Despiertas en una playa desierta. Puedes ir a selva o a cueva.")

        historia_selva = Historia(1002, "selva", "Estás en la selva. Hay un río y un sendero.")
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


TOKEN = "7063061533:AAES88sHhQ-kgppCPIuuRVU0rAC-R0Z3Q5A"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # chat_id = update.effective_chat.id
    # if chat_id not in sesiones:
    #    sesiones[chat_id] = Sesion(chat_id, historia_principal.id, historias)
    await update.message.reply_text("¡Bienvenido al juego de historias! "
                                    "\nEscribe /play para comenzar."
                                    "\nEscribe /help para explicarte mi funcionamiento.")


async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # AÑADIR LO DE SESIONES
    await update.message.reply_text("Al escribir /play se contará una historia, de la cual "
                                    "tienes que elegir entre 2 caminos, ¿Como los eliges? "
                                    "Pues simplemente escribiendo la palabra clave del camino.")


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hola")


if __name__ == "__main__":

    myBot = telegram.Bot(token=TOKEN)  # Bot con el TOKEN

    # Crea una instancia de Application
    application = Application.builder().token(myBot.token).build()

    # Añade manejadores para los comandos
    application.add_handler(CommandHandler("start", start))  # AQUI AÑADIR MAS OPCIONES
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("help", ayuda))

    # Inicia el bot y espera eventos (polling)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
