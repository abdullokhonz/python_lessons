import telebot

bot = telebot.TeleBot('7005186553:AAEbOVbVnQKOZ1R7y4q9aUHEbmbnyalFH8c')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.infinity_polling()
