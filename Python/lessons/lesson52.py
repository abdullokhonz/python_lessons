import telebot
import requests
from ..tg_tokens import token_lesson52 as token

bot = telebot.TeleBot(token.TOKEN)
API = token.API


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip()
    result = requests.get(
        url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'
    )

    if result.status_code == 200:
        temp = round(result.json()['main']['temp'])
        photo = open('img_w/warm.jpg', 'rb') if temp > 0 else open('img_w/cold.jpg', 'rb')
        bot.send_message(message.chat.id, f'В городе {city} сейчас {temp} градусов!')
        bot.send_photo(message.chat.id, photo)
        photo.close()
    else:
        bot.send_message(message.chat.id, 'Неизвестный город!')


bot.infinity_polling()
