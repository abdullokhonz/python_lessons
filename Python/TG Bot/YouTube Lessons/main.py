import telebot
from ...tg_tokens import token_main as token

bot = telebot.TeleBot(token.TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.infinity_polling()
