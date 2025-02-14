import telebot
from ..tg_tokens import token_lesson49 as token

TOKEN = token.TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello World!')


bot.infinity_polling()
