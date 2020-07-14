import telegram 
from telegram.ext import *

mi_bot = telegram.Bot(token="1255840202:AAESK__tlVGY63FVPJOJufa70DLej8UfXrI")
mi_bot_updater = Updater(mi_bot.token)

def start(bot,update, pass_chat_data=True):
    update.message.chat_id # ide de cada chat con cada persona, actualizar mensaje por cada ID 
    bot.sendMessage(chat_id=update.message.chat_id, text="prueba Telegram")

def start2(bot,update, pass_chat_data=True):
    update.message.chat_id # ide de cada chat con cada persona, actualizar mensaje por cada ID 
    bot.sendMessage(chat_id=update.message.chat_id, text="segundo mensaje ")

start_handler = CommandHandler('start',start)
start_handler2 = CommandHandler('sterling',start2)


dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(start_handler2)

mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
    pass

