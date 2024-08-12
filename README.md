# TFG-Chatbot-eleccion-caminos

Esta aplicación es parte del Trabajo de Fin de Grado en 
Ingeniería Informática por parte de Pablo Pérez Paramos.
La aplicación consiste en un bot el cual mediante una API 
de Telegram cuenta una historia y da la posibilidad de 
elegir el siguiente camino de la misma.

## Características principales

- Característica 1:
- Característica 2:

## Tecnologías utilizadas

- Python, API python-telegram-bot, Base de Datos SQLite

## Elementos necesarios para la ejecucición del Proyecto

- Python 3.11.3 o superior

- python-telegram-bot v21.4 o superior. Instálalo utilizando el siguiente comando en la línea de comandos:
```bash
> pip install python-telegram-bot --upgrade
```

- python-dotenv

- Crear el bot en Telegram. Donde hay que seguir los siguientes pasos:

1. Buscar el usuario `@BotFather` en Telegram.
2. Enviarle el comando `/newbot` para crear el nuevo bot.
3. Elegir un nombre y nombre de usuario para el bot. En este caso elegí `ppparamos-tfg` y `ppparamos-tfgbot` respectivamente.
4. Obtendremos un token de acceso que será necesario para interactuar con la API de Telegram. El cuál se añade en el código.

## Despliegue

Sigue estos pasos para realizar el despliegue de la aplicación:

1. Una vez creado el bot correctamente y demás simplemente tenemos que desplegar nuestro código o mediante el siguiente comando o ejecutandolo desde nuestro IDE.
```bash
> python bot.py
```

Una vez realizados estos pasos el bot quedará encendido y ya podremos hablar con el mediante Telegram. Con el comando `/start` o `/help`.