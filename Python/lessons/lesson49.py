import telebot

TOKEN = '7396159893:AAFSWzBJqHFRSSVzw5tl7XaJTypIqJC4NLY'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello World!')


bot.infinity_polling()
