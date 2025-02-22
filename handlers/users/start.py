from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from random import randint
from loader import dp
from keyboards.default.minu import menu_start

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    await message.answer('asalomu ',reply_markup=menu_start)
@dp.message_handler(text="Math")
async def random(message: types.Message) :

    url=f"http://numbersapi.com/{randint(1,1000)}"
    request=requests.get(url)

    await message.answer(request.content)


@dp.message_handler(text="Date")
async def random(message: types.Message) :

    url=f"http://numbersapi.com/{randint(1,1000)}"
    request=requests.get(url)

    await message.answer(request.content)

@dp.message_handler(text="Trivia")
async def random(message: types.Message) :

    url=f"http://numbersapi.com/{randint(1,1000)}"
    request=requests.get(url)

    await message.answer(request.content)




