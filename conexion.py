

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from ibm_watson import ApiException

#------------********** CONEXION CON WATSON ***************---------------

def conexion():
    try:
        authenticator = IAMAuthenticator('VZHzvjelK9YsjuYtBGOkXhFLhoDGruweoDcYIfKhE7hT')
        assistant = AssistantV2(
            version='2018-09-20',
            authenticator=authenticator,

        )
        # assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')
        assistant.set_disable_ssl_verification(True)
        assistant.set_service_url(
            'https://api.us-east.assistant.watson.cloud.ibm.com/instances/1b62e879-1f7e-4e0b-9d72-5ab9c1d9328b')
        session = assistant.create_session('a8817251-2b48-47d0-a208-09f7fde9b369').get_result()
        session_id = session["session_id"]
    except ApiException as ex:
        print("Metodo fallo " + str(ex.code) + ": " + ex.message)

def obtenerMensaje(assistant,session_id, mensaje):
    message = assistant.message(
        'a8817251-2b48-47d0-a208-09f7fde9b369',
        session_id,
        input={'text': mensaje},
        context={
            'metadata': {
                'deployment': 'myDeployment'
            }
        }).get_result()

    output = message['output']
    generic = output['generic']
    map = generic[0]
    # si la respuesta es solo texto, al trabajar con respuestas co imagenes cambiar el codigo
    respuesta = map['text']
    return respuesta

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
    #update.message.text=1
    '''try:
        authenticator = IAMAuthenticator('VZHzvjelK9YsjuYtBGOkXhFLhoDGruweoDcYIfKhE7hT')
        assistant = AssistantV2(
            version='2018-09-20',
            authenticator=authenticator,

        )
        # assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')
        assistant.set_disable_ssl_verification(True)
        assistant.set_service_url(
            'https://api.us-east.assistant.watson.cloud.ibm.com/instances/1b62e879-1f7e-4e0b-9d72-5ab9c1d9328b')
        session = assistant.create_session('a8817251-2b48-47d0-a208-09f7fde9b369').get_result()
        session_id = session["session_id"]
    except ApiException as ex:
        print("Metodo fallo " + str(ex.code) + ": " + ex.message)

    update.message.text=obtenerMensaje(assistant,session_id, update.message.text)
    persona = update.message.from_user
    print(persona)
    #update.message.text=update.message.text+' '+persona['first_name']+'\n '+' Soy un asistente virtual '
    print(update.message.text)'''
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Hola')
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker='CAADAgADOQADfyesDlKEqOOd72VKAg')
    context.bot.send_audio(chat_id=update.effective_chat.id,
                             audio='http://www.largesound.com/ashborytour/sound/brobob.mp3')
    context.bot.send_animation(chat_id=update.effective_chat.id,
                             animation='http://images6.fanpop.com/image/photos/37800000/-Hello-penguins-of-madagascar-37800672-500-500.gif')
    context.bot.send_location(chat_id=update.effective_chat.id,
                             latitude=51.521727,
                              longitude=-0.117255)
    '''# Send document
    bot$sendDocument(chat_id,
                     document="https://github.com/ebeneditos/telegram.bot/raw/gh-pages/docs/telegram.bot.pdf"
                     )'''

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
    conexion()
    main()