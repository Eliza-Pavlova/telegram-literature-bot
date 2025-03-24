import telebot
from telebot import types
import requests
import random
from bs4 import BeautifulSoup

TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

url = "https://znanierussia.ru/articles/%D0%9B%D0%B8%D0%BD%D0%B3%D0%B2%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0"
data = requests.get(url)

if data.status_code == 200:
    pass
else:
    print('error')

page = BeautifulSoup(data.content, "html.parser")


def find_resources():
    headers = page.find_all(['h2', 'h3'])

    literature_found = False
    for header in headers:
        if 'Литература' in header.get_text():
            literature_found = True
            sources_list = header.find_next('ul')

            if sources_list:
                sources = [li.get_text() for li in sources_list.find_all('li')]

                return sources
            else:
                print("Список источников не найден.")
            break

    if not literature_found:
        print("Раздел 'Литература' не найден.")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет!")
    text = "Напишите /list, чтобы вывести весь список литературы\nНапишите /random, чтобы вывести случайный источник."
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('/list')
    button_2 = types.KeyboardButton('/random')
    kb.add(button_1, button_2)
    bot.send_message(message.chat.id, text, reply_markup=kb)

@bot.message_handler(commands=['list'])
def list_currencies(message):
    sources = find_resources()
    if sources:
        formatted_sources = '\n'.join(f"{index + 1}. {source}" for index, source in enumerate(sources))
        bot.send_message(message.chat.id, f"Список литературы:\n{formatted_sources}")
    else:
        bot.send_message(message.chat.id, "Источники не найдены.")

@bot.message_handler(commands=['random'])
def random_resources(message):
    sources = find_resources()
    if sources:
        random_source = random.choice(sources)
        bot.send_message(message.chat.id, f"Случайный источник: {random_source}")
    else:
        bot.send_message(message.chat.id, "Источники не найдены.")

if __name__ == 'main':
    bot.polling()
