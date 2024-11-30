import telebot
import  json
from telebot import types
import control
bot=telebot.TeleBot('5913196526:AAH3tDOirx2EL5nqCWnULZVKt74BCSLrQ1o')
@bot.message_handler(commands=['start'])
def start(message):
    menu=types.ReplyKeyboardMarkup(row_width=1)
    url=types.KeyboardButton('Перейти на сайт',web_app=types.WebAppInfo('https://coder1382.github.io/Supplement-to-WEB-App-Telebot/'))
    menu.add(url)
    bot.send_message(message.chat.id,'<em>Нажмите на кнопку, чтобы зайти в приложение</em>',reply_markup=menu,parse_mode='html')
@bot.message_handler(content_types=['web_app_data'])
def web(message):
    data=json.loads(message.web_app_data.data)
    bot.send_message(message.chat.id,f'<em>Имя заказчика:</em>  <b>{data["name"]}</b>\n<em>Эл.почта заказчика:</em>  <b>{data["email"]}</b>\n<em>Телефон заказчика:</em>  <b>{data["phone"]}</b>\n<em>Заказ:  </em><b>{json.loads(data["food"])}</b>',parse_mode='html')
    control.bot.send_message(message.chat.id,f'<em>Имя заказчика:</em>  <b>{data["name"]}</b>\n<em>Эл.почта заказчика:</em>  <b>{data["email"]}</b>\n<em>Телефон заказчика:</em>  <b>{data["phone"]}</b>\n<em>Заказ:  </em><b>{json.loads(data["food"])}</b>',parse_mode='html')
bot.polling(none_stop=True)