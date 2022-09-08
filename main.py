import telebot
import datetime
from pyowm import *
from pyowm.utils.config import get_default_config

language = get_default_config()
language['language'] = 'ru'
owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410', language)
mgr = owm.weather_manager()

bot = telebot.TeleBot('5771225512:AAE7xi9cS4NpDQjJtYQXLL3b26xwcJIrZqs')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('привет', 'пока')
keybord1.row('какая сегодня дата?', 'какой сегодня день недели?')
keybord1.row('погода')

weath = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello', reply_markup=keybord1)




@bot.message_handler(content_types=['text'])
def send_text(message):
    global weath
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'и тебе привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'и тебе пока')
    elif message.text.lower() == 'какая сегодня дата?':
        bot.send_message(message.chat.id, datetime.date.today())
    elif message.text.lower() == 'какой сегодня день недели?':
        days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        bot.send_message(message.chat.id, days[datetime.datetime.today().weekday()])
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Введите город')
        weath = True
    elif weath == True:
        ans = mgr.weather_at_place(message.text)
        ans = ans.weather
        out = f"Облачность: {ans.clouds} %\n" \
              f"Текущая температура: {ans.temperature('celsius').get('temp')} градусов\n" \
              f"Максимальная температура: {ans.temperature('celsius').get('temp_max')} градусов\n" \
              f"Минимальная температура: {ans.temperature('celsius').get('temp_min')} градусов\n" \
              f"Сейчас ощущается: {ans.temperature('celsius').get('feels_like')} \n" \
              f"За последний час выпало осадков: {ans.rain.get('1h', '0')} мм \n" \
              f"Скорость ветра: {ans.wind()['speed']} м/c"
        # out = 'Облачность: ' + str(ans.clouds) + '%\nТекущая температура: ' + str(ans.temperature('celsius').get('temp')) + ' градусов\nМаксимальная температура: ' + str(ans.temperature('celsius').get('temp_max')) + ' градусов\nМинимальная температура: ' + str(ans.temperature('celsius').get('temp_min')) + ' градусов\nСейчас ощущается: ' + str(ans.temperature('celsius').get('feels_like')) + '\nЗа последний час выпало осадков: ' + str(ans.rain.get('1h', '0')) + ' мм'
        bot.send_message(message.chat.id, out)
        weath = False

bot.polling()
