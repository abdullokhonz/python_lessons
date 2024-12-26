import telebot
import requests

bot = telebot.TeleBot('7332524337:AAGjs1XB2aDtmKVijXFjgAgB60GoxYg8_xY')
API = 'fa688ebab2a48fdda4b7e3c8d9818857'


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
