import telebot
from telebot.types import KeyboardButton

def get_main_kb():
    todays_tempurature_btn = telebot.types.KeyboardButton(text="/today")

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True , one_time_keyboard= False , )
    keyboard.row (todays_tempurature_btn)
    
    return keyboard