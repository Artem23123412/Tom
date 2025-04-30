import keyboards
from aiogram import Router
from dotenv import load_dotenv
import os
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.filters.command import Command
import gpt_service



load_dotenv()


TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
router = Router()
dp = Dispatcher()


@router.message(Command("start"))
async def start(message):
    await message.answer("Привет! Меня зовут Том и я помогу тебе с фразеологизмами", reply_markup=keyboards.start_keyboard())


@router.message(Command("help"))
async def help(message):
    await message.answer("Я буду исправлять ошибки в предложением", reply_markup=keyboards.start_keyboard())


@router.message(Command("about"))
async def about(message):
    await message.answer("Здравствуй! Я бот Том. Напиши своё предложение, и я постараюсь сделать его лучше, добавив нужные фразеологизмы и исправив ошибки.", reply_markup=keyboards.start_keyboard())


@router.message()
async def processing_of_phraseological_units(message):
    chatresult = await gpt_service.check_phraseological(message.text)
    await message.answer(chatresult)

    

dp.include_router(router)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())