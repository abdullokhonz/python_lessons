import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

bot.send_message(6111655713, 'Restart')


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(
        message.chat.id,
        'Добро пожаловать!'
        '\n--------\n'
        'Welcome!')
    user_info: str = (f'First name: {message.from_user.first_name}\n'
                      f'Last name: {message.from_user.last_name}\n'
                      f'Username: @{message.from_user.username}\n'
                      f'ID: {message.from_user.id}\n'
                      f'Language: {message.from_user.language_code}')
    bot.send_message(6111655713, user_info)


@bot.message_handler(content_types=['text'])
def bot_text(message):
    bot.send_message(
        message.chat.id,
        'Это бета-версия бота.\nСкоро выйдет полная версия бота!'
        '\n--------\n'
        'This is a beta version of the bot.\nThe full version of the bot will be released soon!'
    )


bot.infinity_polling()
