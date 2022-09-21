import telebot
import requests
import json

TOKEN = '5487683906:AAED5AuLe4wU14cR2THvtQpXCvh5T2y5e9I'
bot = telebot.TeleBot(TOKEN)


keys = {
            'биткоин': 'BTC',
            'эфириум': 'ETH',
            'доллар': 'USD'
            }


@bot.message_handler(commands = ['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Приветствие!'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types = ['text'])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling(non_stop = True)









