import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from server.historia import Historia
from server.sesion import Sesion
from server.servidor import Servidor

# Inicializa las historias y sesiones
servidor = Servidor()
historias = servidor.historia_actual()
sesiones = servidor.sesiones()

historia_inicial = historias.buscar_historia_por_id(1001)


TOKEN = "7063061533:AAES88sHhQ-kgppCPIuuRVU0rAC-R0Z3Q5A"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    if chat_id not in sesiones:
        sesiones.append(Sesion(chat_id, historia_inicial.id, historias))
    await update.message.reply_text("¡Bienvenido al juego de historias! "
                                    "\nEscribe /play para comenzar."
                                    "\nEscribe /help para explicarte mi funcionamiento.")


async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # AÑADIR LO DE SESIONES
    await update.message.reply_text("Al escribir /play se contará una historia, de la cual "
                                    "tienes que elegir entre 2 caminos, ¿Como los eliges? "
                                    "Pues simplemente escribiendo la palabra clave del camino.")


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(historia_inicial.descripcion)


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
