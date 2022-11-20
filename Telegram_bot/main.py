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

storage = MemoryStorage()  # FSM

# инициализируем бота
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

# инициализируем диспетчер к нашему боту
dp = Dispatcher(bot, storage=storage)  # хранилище состояний в оперативной памяти

# включаем логирование
logging.basicConfig(filename='log.txt',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s %(message)s',
                    level=logging.INFO)


# # создаем handler на команду /Check me
# # по сути мы указываем боту на какую команду будем реагировать
# @dp.message_handler(commands='start')
# # после задаем функцию, которая отправит сообщение на заданную команду
# async def cmd_test1(message: types.Message):
#     # на посланную команду бот сделает reply своим сообщением
#     await message.reply("I'm working, sir")


@dp.message_handler(Command('start'), state=None)  # задаем название команды start
async def welcome(message):
    joinedFile = open('user.txt', 'r')  # создаем файл в который будем записывать id пользователя
    joinedUsers = set()
    for line in joinedFile:  # цикл в котором проверяем имеется ли такой id в файле user
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:  # делаем запись в файл user нового id
        joinedFile = open('user.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)
        joinedFile.close()

    # после проверки и записи выводим сообщение с именем пользователя и отображаем кнопки
    await bot.send_message(message.chat.id, f'ПРИВЕТ, *{message.from_user.first_name},* БОТ РАБОТАЕТ',
                           reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(commands=['mailing_list'])
# задаем функцию обработчик
async def mailing_list(message: types.Message):
    # сверяем id пославшего сообщение с id админа
    if message.chat.id == config.admin:
        # отправляем сообщение
        await bot.send_message(message.chat.id, f'Рассылка началась'
                                                f'\nБот оповестит, когда закончит рассылку',
                               parse_mode=types.ParseMode.MARKDOWN_V2)
        # задаем переменные для хранения принявших и заблокировавших
        recieve_users, block_users = 0, 0
        # открываем user.txt в режиме чтения
        with open('user.txt', 'r') as file:
            # создаем множество всех пользователей
            joined_users = set()
            # проходим циклу по всем id в файле
            for line in file:
                # добавляем во множество id
                joined_users.add(line.strip())
            # запускаем цикл
            for user in joined_users:
                try:
                    await bot.send_photo(user, open('photo.png', 'rb'))
                    recieve_users += 1
                except:
                    block_users += 1
                await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, f'Рассылка завершена \n'
                                                    f'Сообщение получили: {recieve_users} пользователей \n'
                                                    f'Заблокировали бота: {block_users}',
                                   parse_mode=types.ParseMode.MARKDOWN_V2)


@dp.message_handler(commands='info')
async def cmd_test2(message: types.Message):
    await message.reply("I'm studying creates Bots")


@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == 'Информация':
        await bot.send_message(
            message.chat.id, text='Информация\nБот создан специально для обучения', parse_mode='Markdown')

    if message.text == 'Статистика':
        await bot.send_message(message.chat.id, text='Хочешь посмотреть статистику бота?', reply_markup=keyboard.stats,
                               parse_mode='Markdown')


# МЫ ПРОПИСАЛИ В КНОПКАХ КОЛБЭК 'join' ЗНАЧИТ И ТУТ МЫ ЛОВИМ 'join'
@dp.callback_query_handler(text_contains='join')
async def join(call: types.callback_query):
    if call.message.chat.id == config.admin:
        count_users = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Вот статистика бота: *{count_users}* человек', parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='У тебя нет админки\n Куда ты полез', parse_mode='Markdown')


# МЫ ПРОПИСАЛИ В КНОПКАХ КОЛБЭК 'cancel' ЗНАЧИТ И ТУТ МЫ ЛОВИМ 'cancel'
@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Ты вернулся в Главное меню. Жми опять кнопки', parse_mode='Markdown')


# создаем точку входа
if __name__ == '__main__':
    # и запускаем нашего бота в режиме start_pilling
    # по сути после этого во время работы нашего бота
    # бот будет постоянно получать и отвечать на сообщения
    executor.start_polling(dp, skip_updates=True)
