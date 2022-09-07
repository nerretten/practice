import telebot
import datetime
bot = telebot.TeleBot('5771225512:AAE7xi9cS4NpDQjJtYQXLL3b26xwcJIrZqs')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('привет', 'пока')
keybord1.row('какая сегодня дата?', 'какой сегодня день недели?')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello', reply_markup=keybord1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'и тебе привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'и тебе пока')
    elif message.text.lower() == 'какая сегодня дата?':
        bot.send_message(message.chat.id, datetime.date.today())
    elif message.text.lower() == 'какой сегодня день недели?':
        days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        bot.send_message(message.chat.id, days[datetime.datetime.today().weekday()])
        bot.send_message(message.chat.id, days[datetime.datetime.today().weekday()])


bot.polling()
