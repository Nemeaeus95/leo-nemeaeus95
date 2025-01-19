import pyowm
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = pyowm.OWM('aa035df792983c4ab2a26587db48cf2e', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wind_dict_in_meters_per_sec = observation.weather.wind()
    speed = wind_dict_in_meters_per_sec['speed']
    deg = wind_dict_in_meters_per_sec['deg']

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура воздуха в районе " + str(temp) + "\n\n"
    answer += "Скорость ветра: " + str(speed) + " м/с" + "\n\n"
    answer += "Направление ветра: " + str(deg) + "\n\n"

    if deg == range(22, 66):
        answer += "Северо-восточный"
    elif deg == range(67, 111):
        answer += "Восточный"
    elif deg == range(112, 156):
        answer += "Юго-восточный"
    elif deg == range(157, 201):
        answer += "Южный"
    elif deg == range(202, 246):
        answer += "Юго-западный"
    elif deg == range(247, 291):
        answer += "Западный"
    elif deg == range(292, 336):
        answer += "Северо-Западный"
    elif deg == range(0, 23):
        answer += "Северный"
    elif deg == range(337, 359):
        answer += "Северный"
    if temp < 10:
        answer += "Сейчас ппц ка холодно, одевайся как танк!"
    elif temp < 20:
        answer += "Сейчас холодно, оденься потеплее."
    else:
        answer += "Температура норм, одевай что угодно."

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
