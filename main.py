import telebot
import requests
import xml.etree.ElementTree as ET
from telebot import types 
from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

def create_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("/start")
    clear_button = types.KeyboardButton("/help")
    keyboard.add(start_button, clear_button)
    return keyboard

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Добрый день. Как вас зовут?")
        rate_dollar = get_dollar_rate()
        print(rate_dollar)
        bot.register_next_step_handler(message, get_name, rate_dollar)
    elif (message.text == "/help"):
        bot.send_message(message.from_user.id, "Этот бот выводит текущий курс доллара. Для начала введи /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Введи /help для справки.")

def get_name(message, dollar):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Рад знакомству, ' + name + '! Курс доллара сегодня ' + str(dollar) + 'р.')
    

def get_dollar_rate():
    usd_rate = float(ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text).find("./Valute[CharCode='USD']/Value").text.replace(",", "."))
    return usd_rate

bot.polling(non_stop=True, interval=0)