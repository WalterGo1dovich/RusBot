import telebot
import random

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

facts = [
    "Россия — самая большая страна в мире.",
    "Транссибирская магистраль — самая длинная железная дорога в мире.",
    "В России более 1000 озёр.",
    "Сибирь — это не только холод, но и невероятная красота.",
    "Русская культура известна на весь мир."
]

quotes = [
    "Служение России — это высший долг каждого гражданина.",
    "Наша сила в объединении и единстве.",
    "Россия всегда будет великой державой!",
]

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Добро пожаловать в RusBot! Напиши /fact для факта о России или /quote для цитаты.")

@bot.message_handler(commands=['fact'])
def fact(msg):
    bot.reply_to(msg, random.choice(facts))

@bot.message_handler(commands=['quote'])
def quote(msg):
    bot.reply_to(msg, random.choice(quotes))

bot.polling()
