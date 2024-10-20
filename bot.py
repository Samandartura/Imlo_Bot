# import logging

# from aiogram import Bot, Dispatcher, executor, types
# from checkWord import checkWord

# API_TOKEN = '8017077663:AAHT5O91iLduVwlspzK7yI8a63jJaNBpzuY'

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def send_welcome(message: types.Message):
#     await message.reply("uz_imlo Botiga Xush Kelibsiz!")

# @dp.message_handler(commands='help')
# async def help_user(message: types.Message):
#     await message.reply("Botdan foydalanish uchun so'z yuboring.")

# @dp.message_handler()
# async def checkImlo(message: types.Message):
#     word = message.text
#     result = checkWord(word)
#     if result['available']:
#         response = f"✅ {word.capitalize()}"
#     else:
#         response = f"❌{word.capitalize()}\n"
#         for text in result['matches']:
#             response += f"✅ {text.capitalize()}\n"
#     await message.answer(response)

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)



import logging
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from checkWord import checkWord  # Sizning mahalliy funksiyangiz

API_TOKEN = '8017077663:AAHT5O91iLduVwlspzK7yI8a63jJaNBpzuY'

# Logging sozlamasi
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Dispatcher alohida
router = Router()  # Router obyekti yaratildi

# Handlerlarni router orqali ro'yxatdan o'tkazish
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.reply("uz_imlo Botiga Xush Kelibsiz!", reply_markup=ReplyKeyboardRemove())

@router.message(F.text == "/help")
async def help_user(message: Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@router.message()
async def checkImlo(message: Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

# Routerni dispatcher bilan bog'lash
dp.include_router(router)

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
