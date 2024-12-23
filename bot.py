import telebot
from telebot import types

bot = telebot.TeleBot('7756911670:AAFpJK8RQRDSIUBGhV51z-NWhBVsRgd8KeQ')
#dp = Dispatcher(bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', url='https://itproger.com'))
    bot.reply_to(message, 'Привет мой друг!', reply_markup = markup)





bot.infinity_polling(allowed_updates=['message', 'callback_query']) #для кнопок удаления и изменения "callback_messege"
bot.polling(non_stop=True) #infiniti_polling непрерывная работа бота
