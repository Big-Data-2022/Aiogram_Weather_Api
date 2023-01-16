# Default modules - Модули по умолчанию
import csv
import random
from os import system
from time import sleep
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
# import logging
import requests
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Created module - Созданный модуль
from core.weather import weather_city
from core.static.stikers import STIKER_001
from core.config import TOKEN, ADMIN_ID_MARSELLE, WEATHER_API, ADMIN_ID_INT_MARSELLE


system("clear")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# with open(f"core/admin/data/UserInfo.csv", "a", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     ID = "ID"
#     USERNAME = "USERNAME"
#     FIRST_NAME = "FIRST_NAME"
#     LAST_NAME = "LAST_NAME"
#     PHONE = "PHONE"
#     writer.writerow((ID, USERNAME, FIRST_NAME, LAST_NAME, PHONE))


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("Зарегистрироваться", request_contact=True)
    )
    photo_start = open("core/static/image/LOGO_BOT.png", "rb")
    await message.answer_photo(photo=photo_start, caption="Привет я бот зарегистрируйся", reply_markup=markup)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("Алматы"), KeyboardButton("Астана"), KeyboardButton("Атырау"),
        KeyboardButton("Тараз"), KeyboardButton("Шымкент"), KeyboardButton("Актобе"),
        KeyboardButton("Караганда"), KeyboardButton("Павлодар"), KeyboardButton("Уральск"),
        KeyboardButton("Семей"), KeyboardButton("Талдыкорган"), KeyboardButton("Усть-Каменогорск"),
    )
    
    
    user_id = message.contact.user_id
    username = message.chat.username
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    phone = message.contact.phone_number

    # with open(f"core/admin/data/UserInfo.csv", "a", encoding="utf-8") as file:
    #     writer = csv.writer(file)

    #     writer.writerow(
    #         (
    #             user_id,
    #             username,
    #             first_name,
    #             last_name,
    #             phone,
    #         )
    #     )
        
    Informations = f"""id: {user_id}
username: @{username}
first_name: {first_name}
last_name: {last_name}
phone: {phone}
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""

    registration_photo = open("core/static/image/REGISTRATION_LOGO.jpg", "rb")
    await bot.send_photo(ADMIN_ID_MARSELLE, registration_photo, Informations)
    await message.answer("Вы успешно зарегистрированы, теперь отправь название любого города!", reply_markup=markup)

    message_count = []
    @dp.message_handler(content_types=["text"])
    async def weather_city_author(message: types.Message):
        get_weather_def = weather_city(message.text)
        message_count.append(random.randint(0, 1))
        await message.reply(get_weather_def)

        if len(message_count) > random.randint(7, 10):
            await message.reply_sticker(random.choice(STIKER_001))
            message_count.clear()

@dp.message_handler(commands=["almaty"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Алматы")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["astana"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Астана")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["atyrau"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Атырау")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["taraz"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Тараз")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["shymkent"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Шымкент")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["aktobe"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Актобе")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["karaganda"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Караганда")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["pavlodar"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Павлодар")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["oral"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Уральск")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["semey"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Семей")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["taldykorgan"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Талдыкорган")
    await message.reply(get_weather_def)

@dp.message_handler(commands=["ust_kamenogorsk"])
async def weather_command(message: types.Message):
    get_weather_def = weather_city("Усть-Каменогорск")
    await message.reply(get_weather_def)

if __name__ == '__main__':
    print("БОТ ЗАПУЩЕН")
    executor.start_polling(dp)