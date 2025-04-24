from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    args = message.get_args()
    if args == "участвую":
        await message.answer("✅ Вы участвуете в розыгрыше!")
    else:
        await message.answer("Привет! Нажми кнопку «Участвовать», чтобы вступить в розыгрыш.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
