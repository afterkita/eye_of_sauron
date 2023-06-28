
#Главная страница
import config
import telebot
import vk_parsing

bot = telebot.TeleBot(config.BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start_dialog(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def No_Miror(message):
    #print(message)
    line = '~'
    arr = vk_parsing.VKrequest(message.text)
    #print(' -- ',arr)
    for i in range(len(arr)):
        line = line+str(arr[i])+'\n'
    bot.send_message(message.chat.id,line)

bot.polling(none_stop=True)

