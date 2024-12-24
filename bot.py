import telebot
from telebot import types

bot = telebot.TeleBot('***')
#dp = Dispatcher(bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    webApp = types.WebAppInfo('https://tokotaty.github.io/WebBot/')
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=webApp))
    bot.reply_to(message, 'Привет мой друг!', reply_markup = markup)

#@bot.message_handler(conte=['start'])




bot.infinity_polling(allowed_updates=['message', 'callback_query']) #для кнопок удаления и изменения "callback_messege"
bot.polling(non_stop=True) #infiniti_polling непрерывная работа бота
