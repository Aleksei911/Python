from aiogram import types, Dispatcher
from Telegram_bots.Pizza_bot.create_bot import dp
from Telegram_bots import Pizza_bot
import json, string


# @dp.message_handler()
async def censorship(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open("cenz.json")))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(censorship)
