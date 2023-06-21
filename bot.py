import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6088589041:AAERXBaGeGOcvtzfbSfGoCNm-b_1u30V-zE"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_hush_kelibsiz(message: types.Message):
    await message.reply("Salom men Sunnat botman Sunnatillo tomonidan yaratilganman")


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
