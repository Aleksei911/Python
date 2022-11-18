from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


start = types.ReplyKeyboardMarkup(resize_keyboard=True) # основа для кнопок

info = types.KeyboardButton('Информация') # кнопка информации
stats = types.KeyboardButton('Статистика') # кнопка статистики

start.add(stats, info)