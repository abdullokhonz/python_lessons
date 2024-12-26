import telebot
from telebot import types
import random
import config
from texts import texts

bot: telebot = telebot.TeleBot(config.TOKEN)

# Хранение состояния игры для каждого пользователя
user_data: dict = {}


# Стартовое сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, texts['start'], parse_mode='html')


# Меню бота
@bot.message_handler(commands=['menu'])
def bot_menu(message):
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add('👤 Профиль')
    markup_menu.add('📋 Информация о боте')
    bot.send_message(message.chat.id, '📒 <b><u>Меню бота</u></b>👇', reply_markup=markup_menu, parse_mode='html')


# Профиль пользователя
@bot.message_handler(func=lambda message: message.text == '👤 Профиль')
def user_profile(message):
    bot.reply_to(
        message,
        texts['user_profile'].format(
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.from_user.id,
            '__ ' * 16,
            ' ' * 8
        ),
        parse_mode='html'
    )


# Информация о боте
@bot.message_handler(func=lambda message: message.text == '📋 Информация о боте')
def bot_information(message):
    bot.reply_to(
        message,
        texts['bot_information'],
        parse_mode='html'
    )


# Помощь с ботом
@bot.message_handler(commands=['help'])
def help_with_bot(message):
    bot.send_message(message.chat.id, texts['help'], parse_mode='html')


# Выбор игр
@bot.message_handler(commands=['games'])
def selection_of_games(message):
    markup_games = types.InlineKeyboardMarkup()
    markup_games.add(types.InlineKeyboardButton('🪨 Камень, ✂️ Ножницы, 🧻 Бумага.', callback_data='rps'))
    markup_games.add(types.InlineKeyboardButton('🔢 Угадай число!', callback_data='guess'))
    bot.send_message(message.chat.id, '⭕ Выберите игру чтобы начать играть:', reply_markup=markup_games)


@bot.callback_query_handler(func=lambda callback: callback.data in ['rps', 'guess'])
def callback_games(callback):
    if callback.data == 'rps':
        rps_game(callback.message)
    elif callback.data == 'guess':
        guess_game(callback.message)


# Камень, Ножницы, Бумага
@bot.message_handler(commands=['rps'])
def rps_game(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'game': 'rps', 'people_s': 0, 'comp_s': 0}
    bot.send_message(chat_id, "<b>👋 Добро пожаловать в игру\n\"🪨 Камень, ✂️ Ножницы, 🧻 Бумага.\"</b>"
                              "\n\n✍️ Введите количество раундов для 🏆 победы:", parse_mode='html')


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('game') == 'rps')
def handle_rps_game(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id, {})
    if 'victory' not in data:
        try:
            victory = int(message.text)
            data['victory'] = victory
            data['rounds'] = 0
            data['people_s'] = 0
            data['comp_s'] = 0
            user_data[chat_id] = data
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🪨 Камень", callback_data="🪨 Камень"))
            markup.add(types.InlineKeyboardButton("✂️ Ножницы", callback_data="️✂️ Ножницы"))
            markup.add(types.InlineKeyboardButton("🧻 Бумага", callback_data="🧻 Бумага"))
            bot.send_message(chat_id, "Игра началась!\n\nВыберите один из вариантов: ⬇️", reply_markup=markup)
        except ValueError:
            bot.send_message(chat_id, "🙏 Пожалуйста, введите число❗")


@bot.callback_query_handler(func=lambda call: user_data.get(call.message.chat.id, {}).get('game') == 'rps')
def handle_rps_choice(call):
    chat_id = call.message.chat.id
    data = user_data.get(chat_id, {})
    people_choice = call.data
    if people_choice in ['🪨 Камень', '✂️ Ножницы', '🧻 Бумага']:
        game_objects = {'🪨 Камень': 1, '✂️ Ножницы': 2, '🧻 Бумага': 3}
        people = game_objects[people_choice]
        comp = random.randint(1, 3)
        result_message = f"👤 Вы выбрали {people_choice}\n🤖 Бот выбрал {list(game_objects.keys())[comp - 1]}.\n"
        if people == comp:
            result_message += "\n<b>🟰 Ничья!</b>\n"
        elif (people == 1 and comp == 2) or (people == 2 and comp == 3) or (people == 3 and comp == 1):
            data['people_s'] += 1
            result_message += "\n<b>✅ Вы победили!</b>\n"
        else:
            data['comp_s'] += 1
            result_message += "\n<b>❌ Вы проиграли!</b>\n"
        data['rounds'] += 1
        user_data[chat_id] = data
        result_message += f"\n🧮 Счёт: {data['people_s']} : {data['comp_s']}"
        if data['people_s'] >= data['victory']:
            result_message += "\n\n<b>🥳 Поздравляем! Вы выиграли игру!</b>"
            user_data.pop(chat_id)
        elif data['comp_s'] >= data['victory']:
            result_message += "\n\n<b>😭 К сожалению, вы проиграли игру.</b>"
            user_data.pop(chat_id)
        else:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🪨 Камень", callback_data="🪨 Камень"))
            markup.add(types.InlineKeyboardButton("✂️ Ножницы", callback_data="✂️ Ножницы"))
            markup.add(types.InlineKeyboardButton("🧻 Бумага", callback_data="🧻 Бумага"))
            bot.send_message(chat_id, "Выберите следующий ход: ⬇️", reply_markup=markup)
        bot.edit_message_text(result_message, call.message.chat.id, call.message.message_id, reply_markup=None,
                              parse_mode='html')


# Угадай число
@bot.message_handler(commands=['guess'])
def guess_game(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "<b>👋 Добро пожаловать в игру\n\"🔢 Угадай число!\"</b>"
                              "\n\n✍️ Введите начальное число:", parse_mode='html')
    user_data[chat_id] = {'game': 'guess', 'state': 'start_number'}


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('game') == 'guess')
def handle_guess_game(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id, {})

    try:
        if data['state'] == 'start_number':
            data['start_number'] = int(message.text)
            data['state'] = 'end_number'
            bot.send_message(chat_id, "✍️ Теперь введите последнее число:")

        elif data['state'] == 'end_number':
            data['end_number'] = int(message.text)
            data['random_number'] = random.randint(data['start_number'], data['end_number'])
            bot.send_message(chat_id, "✍️ Введите количество попыток:")
            data['state'] = 'attempts'

        elif data['state'] == 'attempts':
            data['attempts'] = int(message.text)
            data['current_attempt'] = 0
            bot.send_message(chat_id, "<b>Начнем игру!</b>\n✍️ Введите число:", parse_mode='html')
            data['state'] = 'guessing'

        elif data['state'] == 'guessing':
            guess = int(message.text)
            data['current_attempt'] += 1

            if guess == data['random_number']:
                bot.send_message(chat_id,
                                 f"🥳 <b>Поздравляем! Вы угадали число {data['random_number']} за \
{data['current_attempt']} попыток!</b>", parse_mode='html')
                user_data.pop(chat_id)  # Очищаем данные после выигрыша

            elif data['current_attempt'] >= data['attempts']:
                bot.send_message(chat_id,
                                 f"😭 <b>У вас закончились попытки. Загаданное число было {data['random_number']}.</b>",
                                 parse_mode='html')
                user_data.pop(chat_id)  # Очищаем данные после проигрыша

            else:
                if guess < data['random_number']:
                    bot.send_message(chat_id, "📈 <b>Загаданное число больше</b>. Попробуйте ещё раз.",
                                     parse_mode='html')
                else:
                    bot.send_message(chat_id, "📉 <b>Загаданное число меньше</b>. Попробуйте ещё раз.",
                                     parse_mode='html')

    except ValueError:
        bot.send_message(chat_id, "🙏 Пожалуйста, введите корректное число❗")


bot.infinity_polling()
