from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
import keyboard

import logging

storage = MemoryStorage() # FSM

# инициализируем бота
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

# инициализируем диспетчер к нашему боту
dp = Dispatcher(bot, storage=storage) # хранилище состояний в оперативной памяти

# включаем логирование
logging.basicConfig(filename='log.txt',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s %(message)s',
                    level=logging.INFO)


# создаем handler на команду /Check me
# по сути мы указываем боту на какую команду будем реагировать
@dp.message_handler(commands='start')
# после задаем функцию, которая отправит сообщение на заданную команду
async def cmd_test1(message: types.Message):
    # на посланную команду бот сделает reply своим сообщением
    await message.reply("I'm working, sir")


@dp.message_handler(commands='info')
async def cmd_test2(message: types.Message):
    await message.reply("I'm studying creates Bots")


# создаем точку входа
if __name__ == '__main__':
    # и запускаем нашего бота в режиме start_pilling
    # по сути после этого во время работы нашего бота
    # бот будет постоянно получать и отвечать на сообщения
    executor.start_polling(dp, skip_updates=True)
