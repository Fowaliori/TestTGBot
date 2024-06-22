import telebot

botTimeWeb = telebot.TeleBot('6286556342:AAE-rqaQ6xwtefzj9fSTbd9jm1ITP7yFejU')

from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"{message.from_user.first_name} , привет!\n Покупка VPN?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  button_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')
  markup.add(button_yes, button_no)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Мы облачная платформа для разработчиков и бизнеса. Более детально можешь ознакомиться с нами на нашем сайте!"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

botTimeWeb.infinity_polling()