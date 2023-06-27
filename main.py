
#Главная страница
import config
import telebot

bot = telebot.TeleBot(config.BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start_dialog(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def Miror(message):
    bot.send_message(message.chat.id,message.text)

bot.polling(none_stop=True)

