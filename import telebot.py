import telebot
from telebot import types

token = '7790178826:AAHzJIiCi9i6nS2-4xIqm74K6CuAcSPcJuY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Приветствую вас! нажмите /button.")

@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('ваше голосове сообщение', callback_data='question_1')
    markup.add(item)
    bot.send_message(message.chat.id, 'Нажмите кнопку:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'question_1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.chat.id,text= "Вы нажали кнопку 'кидайте свое голосовое сообщение!")

bot.infinity_polling()