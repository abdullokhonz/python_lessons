import telebot
import sqlite3

bot = telebot.TeleBot('7332524337:AAGjs1XB2aDtmKVijXFjgAgB60GoxYg8_xY')


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать')
    db = sqlite3.connect("db/myDB")
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            password TEXT
        )
    ''')
    db.commit()

    cursor.close()
    db.close()

    bot.send_message(message.chat.id, "Сейчас вас зарегистрируем! Введите ваше имя")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    name = message.text

    bot.send_message(message.chat.id, f"{name}! Введите пароль")
    bot.register_next_step_handler(message, get_pass, name)  # Передали имя в следующую функцию


def get_pass(message, name):
    password = message.text

    db = sqlite3.connect("db/myDB")
    cursor = db.cursor()

    cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))  # Добавление в таблицу
    db.commit()
    cursor.close()
    db.close()

    bot.send_message(message.chat.id, "Вы успешно зарегистрировались!")


bot.polling(none_stop=True)
