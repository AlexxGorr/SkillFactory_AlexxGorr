import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands = ['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в формате: \n- имя валюты \
- в какую валюту перевести \
- количество переводимой валюты \nУвидеть список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.send_message(message.chat.id, text)


# @bot.message_handler(content_types = ['text'])
# def convert(message: telebot.types.Message):
#     try:
#         values = message.text.split(' ')
#
#         if len(values) != 3:
#             raise ConvertionException('Слишком много параметров.')
#
#         quote, base, amount = values
#         total_base = CryptoConverter.convert(quote, base, amount)
#     except ConvertionException as e:
#         bot.reply_to(message, f'Ошибка пользователя\n{e}')
#     except Exception as e:
#         bot.reply_to(message, f'Не удалось обработать команду\n{e}')
#     else:
#         text = f'Цена {amount} {quote} в {base} - {total_base}'
#         bot.send_message(message.chat.id, text)

@bot.message_handler(commands = ['convert'])
def values(message: telebot.types.Message):
    text = 'Выбери валюту из которой конвертировать: '
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, quote_handler)

def quote_handler(message: telebot.types.Message):
    base = message.text.strip()
    text = 'Выбери валюту в которую конвертировать: '
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, base_handler, base)

def base_handler(message: telebot.types.Message, quote):
    sym = message.text.strip()
    text = 'Количество конвертируемой валюты: '
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, quote, base)

def amount_handler(message: telebot.types.Message, quote, base):
    amount = message.text.strip()
    try:
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.send_message(message.chat.id, f'Ошибка конвертации\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)



bot.polling(non_stop = True)

























