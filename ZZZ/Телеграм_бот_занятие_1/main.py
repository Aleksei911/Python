import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

# подключение модуля с токеном
import config
# подключение модуля с кнопками
import keyboard

"""-------------------------------------- настройка бота и логирование -------------------------------------------"""

# хранилище состояний
storage = MemoryStorage()
# инициализация бота
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
# инициализация диспетчера, при этом указываем ему на хранилище состояний
dp = Dispatcher(bot, storage=storage)
# подключаем логирование
logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')

""" -------------------------------------- обработка команды /start ----------------------------------------------"""


# подключаем handler на команду start, указываем состояние равное None
@dp.message_handler(commands='start', state=None)
async def welcome(message: types.Message):
    # открываем файл user.txt в режиме чтения
    joined_file = open('user.txt', 'r')
    # создаем множество для хранения имен всех пользователей
    joined_users = set()
    # проходим циклом по каждому пользователю в user.txt
    for line in joined_file:
        # добавляем их в наше множество пользователей
        joined_users.add(line.strip())
    # если пользователь, который нажал /start
    # находится во множестве пользователей
    if not str(message.chat.id) in joined_users:
        # открываем файл user.txt на дозапись
        joined_file = open('user.txt', 'a')
        # записываем в него id нашего пользователя
        joined_file.write(str(message.chat.id) + '\n')
        # добавляем его во множество пользователей
        joined_users.add(message.chat.id)
        # говорим боту отправить сообщение, при этом
    await bot.send_message(
        # обращаемся к id пользователя
        message.chat.id,
        # указываем отправляемое сообщение hello + имя пользователя
        f'Hello __{message.from_user.first_name}__',
        # подключаем кнопки из файла keyboard, обратившись к переменной start
        reply_markup=keyboard.start)


""" -------------------------------------- кнопка /Информация -------------------------------------------------"""


# задаем обработчик для нашей кнопки, указываем тип контента как text
@dp.message_handler(content_types=['text'])
# задаем функцию-обработчик
async def info(message: types.Message):
    # если переданное боту сообщение = 'Информация'
    if message.text == 'Информация':
        # бот отправляет сообщение пользователю, отправившего его
        await bot.send_message(message.chat.id,
                               # с текстом
                               text='Бот \nсоздан в образовательных целях',
                               # режим форматирования
                               parse_mode='Markdown')


""" -------------------------------------- точка входа --------------------------------------------------------"""
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
