import telebot

bot = telebot.TeleBot('822463728:AAFXQda1KPDLuCX59n44ya_L_Kb_S9hc6qQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вас приветствует робот-консультант Госуслуг!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Здравствуйте! Чем я могу вам помочь?")
    elif message.text.lower() == 'спасибо':
        bot.send_message(message.chat.id, "Был рад помочь вам! Обращайтесь!")
    elif message.text.lower() == 'номер поддержки':
        bot.send_message(message.chat.id, "Позвонить в службу поддержки вы можете по телефону 8-800-555-00-00")

bot.polling()