import telebot
from DataBase import *

bot = telebot.TeleBot('6286556342:AAE-rqaQ6xwtefzj9fSTbd9jm1ITP7yFejU')

from telebot import types

@bot.message_handler(commands=['start'])
def startBot(message):

    firstMessage = f"{message.from_user.first_name} , привет!\nПокупка VPN?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    button_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')
    markup.add(button_yes, button_no)
    bot.send_message(message.chat.id, firstMessage, reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
    if function_call.data == "yes":
        secondMessage = "Покупка VPN проходит через перевод..."
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Оплатил", callback_data='buy'))
        bot.send_message(function_call.message.chat.id, secondMessage, parse_mode='html', reply_markup=markup)
        bot.answer_callback_query(function_call.id)
    elif function_call.data == "buy":
        confirmMessage = "VPN был куплен"
        bot.send_message('655271075', function_call.message.chat.id)
        bot.send_message(function_call.message.chat.id, confirmMessage)
        bot.answer_callback_query(function_call.id)
        conn = psycopg2.connect(dbname="testtgbase", user="postgres", password="123", host="127.0.0.1", port="5959")
        cursor = conn.cursor()
        today = datetime.now().date()
        info = (function_call.message.chat.id, today.strftime("%Y-%m-%d"))
        print(info)
        cursor.execute("INSERT INTO userstg (userid, datestart) VALUES (%s %s)", info)
    elif function_call.data == "no":
        messageAnswer(function_call.message)
        bot.answer_callback_query(function_call.id)

@bot.message_handler(content_types=['text'])
def messageAnswer(message):
    defaultMessage = "Я бот для покупки VPN, чтобы начать пользоваться напиши /start"
    bot.send_message(message.chat.id, defaultMessage)
bot.infinity_polling()

