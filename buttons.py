from telebot import types
import cfg

func_btn = types.ReplyKeyboardMarkup()
link_btn = types.InlineKeyboardMarkup()
back_btn = types.ReplyKeyboardMarkup()
clear = types.ReplyKeyboardRemove()

item0 = types.KeyboardButton('ChatGPT')

item7 = types.KeyboardButton('Назад')

func_btn.add(item0)
#link_btn.add(item8)
back_btn.add(item7)