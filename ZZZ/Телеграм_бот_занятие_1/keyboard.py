from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

# добавляем разметку наших кнопок
start = types.ReplyKeyboardMarkup(resize_keyboard=True)
# создаем кнопки информация
info = types.KeyboardButton('Информация')
# и статистика
stats = types.KeyboardButton('Статистика')
# добавляем кнопки в нашу разметку
start.add(stats, info)
