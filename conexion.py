

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# conexion con bot Telegram, token de API
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """comando start"""
    update.message.reply_text('Bienvenido a este humilde bot 🤖 ')


def help_command(update, context):
    """comando help"""
    update.message.reply_text('Help!')


def echo(update, context):
    """mostrar mensaje en pantalla"""
    print(update.message.text)
    update.message.reply_text(update.message.text)

def sumar(update, context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        suma = numero1 + numero2

        update.message.reply_text("La suma es "+str(suma))

    except (ValueError):
        update.message.reply_text("Que quieres que sume letras, no seas tonto 😑  ")

def multiplicar(update, context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        multiplicacion = numero1 * numero2

        update.message.reply_text("La multiplicacion es "+str(multiplicacion))

    except (ValueError):
        update.message.reply_text("Que quieres que multiplique letras, no seas tonto 😑   ")

def dividir(update, context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        division = numero1 / numero2

        update.message.reply_text("La division es "+str(division))

    except (ValueError):
        update.message.reply_text("Que quieres que divida letras, no seas tonto 😑   ")

def restar(update, context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        resta = numero1 - numero2

        update.message.reply_text("La resta es "+str(resta))

    except (ValueError):
        update.message.reply_text("Que quieres que resta letras, no seas tonto 😑   ")

def main():
    """Start the bot."""

    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1255840202:AAESK__tlVGY63FVPJOJufa70DLej8UfXrI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # diferentes comandos - respuestas en Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("sumar", sumar))
    dp.add_handler(CommandHandler("restar", restar))
    dp.add_handler(CommandHandler("multiplicar", multiplicar))
    dp.add_handler(CommandHandler("dividir", dividir))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()