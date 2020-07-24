
#Import Bot telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Imbort IBM watson
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from ibm_watson import ApiException

class Chatbot():

    def __init__(self, tokenTelegram, ibm_apiKey, ibm_url, ibm_assitantId):
        self.sessionId=''
        self.assistant=None
        self.assistantId=ibm_assitantId

        self.sessionId= self.conexionIbm(ibm_apiKey,ibm_url,ibm_assitantId)

        # Conexion con el bot
        self.updater=Updater(tokenTelegram,use_context=True)
        self.dispatcher= self.updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

        #handler para un comando start
        self.start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(self.start_handler)

        #handler para un comando sumar
        self.sumar_handler = CommandHandler('sumar', self.sumar)
        self.dispatcher.add_handler(self.sumar_handler)

        # handler para un comando restart
        self.restar_handler = CommandHandler('restar', self.restar)
        self.dispatcher.add_handler(self.restar_handler)

        # handler para un comando multiplicar
        self.multiplicar_handler = CommandHandler('multiplicar', self.multiplicar)
        self.dispatcher.add_handler(self.multiplicar_handler)

        # handler para un comando dividir
        self.dividir_handler = CommandHandler('dividir', self.dividir)
        self.dispatcher.add_handler(self.dividir_handler)

        # handler para cuando es un mensaje texto
        self.texto_handler = MessageHandler(Filters.text, self.echo)
        self.dispatcher.add_handler(self.texto_handler)

        #iniciar bot
        self.updater.start_polling()
        self.updater.idle()


    #--------- Seccion por Comandos ----------
    def start(self,update, context):
        """comando start"""
        update.message.reply_text('Bienvenido a este humilde bot 🤖 ')

    def help_command(self, update, context):
        """comando help"""
        update.message.reply_text('Help!')

    #------------ Seccion para mensaje simple --------
    def echo(self, update, context):
        persona = update.message.from_user
        print("Nombre usuario: "+persona['first_name']+" Mensaje: "+update.message.text)
        if(update.message.text =='hola'):
            update.message.text='Hola '+persona['first_name']+'\n '+' Soy un asistente virtual y estoy aqui para ayudarte '
        else:
            update.message.text=self.obtenerMensaje(update.message.text, self.sessionId)

        update.message.reply_text(update.message.text)


    #------------- Operaciones Matematicas Basicas --------------
    def sumar(self, update, context):
        try:
            numero1 = int(context.args[0])
            numero2 = int(context.args[1])

            suma = numero1 + numero2

            update.message.reply_text("La suma es " + str(suma))

        except (ValueError):
            update.message.reply_text("Que quieres que sume letras, no seas tonto 😑  ")

    def restar(self, update, context):
        try:
            numero1 = int(context.args[0])
            numero2 = int(context.args[1])

            resta = numero1 - numero2

            update.message.reply_text("La resta es " + str(resta))

        except (ValueError):
            update.message.reply_text("Que quieres que resta letras, no seas tonto 😑   ")

    def multiplicar(self,update, context):
        try:
            numero1 = int(context.args[0])
            numero2 = int(context.args[1])

            multiplicacion = numero1 * numero2

            update.message.reply_text("La multiplicacion es " + str(multiplicacion))

        except (ValueError):
            update.message.reply_text("Que quieres que multiplique letras, no seas tonto 😑   ")

    def dividir(self, update, context):
        try:
            numero1 = int(context.args[0])
            numero2 = int(context.args[1])

            division = numero1 / numero2

            update.message.reply_text("La division es " + str(division))

        except (ValueError):
            update.message.reply_text("Que quieres que divida letras, no seas tonto 😑   ")

    def conexionIbm(self, apiKey, url, assitantId):
        try:
            authenticator = IAMAuthenticator(apiKey)
            self.assistant = AssistantV2(
                version='2018-09-20',
                authenticator=authenticator,

            )
            # assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')

            self.assistant.set_disable_ssl_verification(False)
            self.assistant.set_service_url(
                url)
            session = self.assistant.create_session(assitantId).get_result()
            sessionId = session["session_id"]
        except ApiException as ex:
            print("Metodo fallo " + str(ex.code) + ": " + ex.message)
        return sessionId

    def obtenerMensaje(self, mensaje, sessionId):

        message = self.assistant.message(
            self.assistantId,
            sessionId,
            input={'text': mensaje},
            context={
                'metadata': {
                    'deployment': 'myDeployment'
                }
            }).get_result()

        try:
            output = message['output']
            generic = output['generic']
            map = generic[0]
            respuesta = map['text']
        except  ApiException as ex:

            print("Fallo obtener mensaje " + str(ex.code) + ": " + ex.message)

        # si la respuesta es solo texto, al trabajar con respuestas co imagenes cambiar el codigo


        return respuesta