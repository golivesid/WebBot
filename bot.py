import telebot
from telebot import types
import os
from dotenv import load_dotenv
import json

load_dotenv()
bot = telebot.TeleBot(os.getenv("6866329408:AAE-uV2sKyCnlCQnZbL9GH_DcdrzsF9omas"))
#dp = Dispatcher(bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    webApp = types.WebAppInfo('https://tokotaty.github.io/WebBot/')
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=webApp))
    bot.send_message(message.chat.id, 'Привет мой друг!', reply_markup = markup)


@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    res = json.loads(message.web_app_data.data)
    bot.send_message(message.chat.id, f'Name: {res["name"]}\nEmail: {res["email"]}\nPhone: {res["phone"]}')




bot.infinity_polling(allowed_updates=['message', 'callback_query'])
bot.polling(non_stop=True)
