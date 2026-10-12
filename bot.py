import telebot
from telebot import types
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('📞 Связаться')
    btn2 = types.KeyboardButton('❓ Частые вопросы')
    btn3 = types.KeyboardButton('🛠 Техподдержка')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Выбери, что тебя интересует:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📞 Связаться')
def send_contact(message):
    bot.reply_to(message, "Связаться со мной: @Твой_Никнейм")

@bot.message_handler(func=lambda message: message.text == '❓ Частые вопросы')
def send_faq(message):
    bot.reply_to(message, "Частые вопросы:\n1. Как оплатить?\n2. Сколько ждать?")

@bot.message_handler(func=lambda message: message.text == '🛠 Техподдержка')
def send_support(message):
    bot.reply_to(message, "Техподдержка: @Никнейм_Админа")

bot.polling(none_stop=True)
