from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для кнопок

info = types.KeyboardButton('Информация')  # кнопка информации
stats = types.KeyboardButton('Статистика')  # кнопка статистики

start.add(stats, info)

"""------------------------------------- СОЗДАЕМ INLINE КНОПКИ------------------------------"""

stats = InlineKeyboardMarkup()  # создаем основу для инлайн кнопок
stats.add(InlineKeyboardButton('Yes', callback_data='join'))  # создаем кнопку и колбэк к ней
stats.add(InlineKeyboardButton('No', callback_data='cancel'))  # создаем кнопку и колбэк к ней
