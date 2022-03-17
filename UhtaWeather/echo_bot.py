import telebot


bot = telebot.TeleBot("", parse_mode = None)
# Вы можете установить parse_mode по умолчанию. HTML или MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
