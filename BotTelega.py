import telebot 
from telebot.types import Message  
 
from constants import BOT_TOKEN 
from parsing import get_parsed_data 
bot = telebot.TeleBot(BOT_TOKEN) 
 
 
@bot.message_handler(commands=['start','hello']) 
def start(message): 
    bot.send_message( 
        message.from_user.id, 
        text=''' 
        Привет! Я твой личный погодный бот. 
        ''', 
    ) 
 
@bot.message_handler(commands=['today']) 
def get_today_weather(message): 
    temperature, discription = get_parsed_data() 
    if temperature is not None and discription is not None: 
        bot.send_message( 
            message.from_user.id, 
            text=f"Сегодня температура в Херсоне {temperature}, прогноз: {discription}", 
        ) 
    else: 
        bot.send_message( 
            message.from_user.id, 
            text = f"Попробуйте в следующий раз" 
        ) 
 
@bot.message_handler(content_types = ['text']) 
def main_message_handler(message): 
    if message.text == 'Сегодня': 
        temperature, discription = get_parsed_data() 
        if temperature is not None and discription is not None: 
            bot.send_message( 
                message.from_user.id, 
                text = f"Сегодня температура в Херсоне {temperature}, прогноз: {discription}", 
            ) 
        else: 
            bot.send_message( 
                message.from_user.id, 
                text = "Не могу получить данные", 
            ) 
    elif message.text == 'Сегодня': 
        bot.send_message( 
            message.from_user.id, 
            text = 'Пожалуйста!' 
        ) 
 
 

if __name__ == "__main__": 
    bot.polling(none_stop = True)