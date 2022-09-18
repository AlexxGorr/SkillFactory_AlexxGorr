import telebot

TOKEN = '5487683906:AAED5AuLe4wU14cR2THvtQpXCvh5T2y5e9I'
bot = telebot.TeleBot(TOKEN)



# обработчик сообщений
# @bot.message_handler(filters)
# def hendle_filters(message):
#     bot.reaply_to(message, 'This is a message handler')


@bot.message_handler(commands = ['start', 'help'])
def hendle_start_help(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f'приветствую {message.chat.username}')


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(non_stop = True)





















