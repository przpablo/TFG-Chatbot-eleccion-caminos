# import os
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# from server.historia import Historia
# from server.sesion import Sesion
from server.servidor import Servidor
from db.models import get_sesion, save_sesion

# Inicializa las historias y sesiones
servidor = Servidor()
historias = servidor.historia_actual()
# sesiones = servidor.sesiones()

historia_inicial = historias.buscar_historia_por_id(1001)

TOKEN = "7063061533:AAES88sHhQ-kgppCPIuuRVU0rAC-R0Z3Q5A"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    if get_sesion(chat_id) is None:
        save_sesion(chat_id, historia_inicial.id)
    await update.message.reply_text("¡Bienvenido al juego de historias! "
                                    "\nEscribe /play para comenzar."
                                    "\nEscribe /help para explicarte mi funcionamiento.")


async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # AÑADIR LO DE SESIONES
    ayuda_texto = ("Al escribir /play se contará una historia, de la cual "
                   "tienes que elegir entre 2 caminos. \n<b>¿Como los eliges?</b> "
                   "Pues simplemente escribiendo la palabra clave del camino. "
                   "\n(Las palabras clave son las palabras que aparecen exclusivamente "
                   "en <b>negrita</b>.)")
    await update.message.reply_text(ayuda_texto, parse_mode='HTML')


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    sesion = get_sesion(chat_id)
    if sesion:
        historia_actual = historias.buscar_historia_por_id(sesion[1])  # NO ESTOY SEGURO
        # historia_actual = historias.buscar_historia_por_id(sesion)
        if historia_actual:
            mensaje = f'{historia_actual.descripcion}'
            await update.message.reply_text(mensaje, parse_mode='HTML')
        else:
            await update.message.reply_text("Error al encontrar la historia actual.")
    else:
        await update.message.reply_text("Por favor, inicia el juego usando /start.")


async def seguir(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    sesion = get_sesion(chat_id)
    if sesion:
        historia_actual = historia_inicial.buscar_historia_por_id(sesion[1])  # NO ESTOY SEGURO

        if historia_actual:
            eleccion = update.message.text.strip().lower()
            nueva_historia = historia_actual.buscar_rama_nombre(eleccion)

            if nueva_historia:
                save_sesion(chat_id, nueva_historia.id)
                await update.message.reply_text(nueva_historia.descripcion, parse_mode='HTML')
            else:
                await update.message.reply_text("Opción no válida. Intenta nuevamente.")
        else:
            await update.message.reply_text("Error al encontrar la historia actual.")
    else:
        await update.message.reply_text("Por favor, inicia el juego usando /start.")


if __name__ == "__main__":

    from db.database import create_tables
    create_tables()

    myBot = telegram.Bot(token=TOKEN)  # Bot con el TOKEN

    # Crea una instancia de Application
    application = Application.builder().token(myBot.token).build()

    # Añade manejadores para los comandos
    application.add_handler(CommandHandler("start", start))  # AQUI AÑADIR MAS OPCIONES
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("help", ayuda))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, seguir))
    # application.add_handler(CommandHandler("seguir", seguir))

    # Inicia el bot y espera eventos (polling)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
