from os import environ

from telegram.ext import Updater
updater = Updater(token=environ['BOT_TOKEN'], use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s -%(level)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()