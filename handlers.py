from aiogram import Router,types
from aiogram.filters import CommandStart,Command
from assets.help_command import *

router = Router()

@router.message(CommandStart())
async def start(message:types.Message):
    await message.answer('Привет!Что-бы узнать команды перейдите в /help')
    await message.delete()

@router.message(Command('help'))
async def help(message:types.Message):
    await message.answer(HELP_COMMAND)

@router.message(Command('help_text'))
async def help_text(message:types.Message):
    await message.answer(HELP_COMMAND_TEXT)

@router.message(Command('stickers'))
async def sticker(message:types.Message):
    await message.reply('Какие милые котики ❤️')
    await message.answer_sticker('CAACAgQAAxkBAAEPTztouoHE5ygaWqT4jOlteUFZ0UyskAACwQ4AAmh_GVMnbKqTMOIbaTYE')

@router.message(Command('fotograpy'))
async def send_image(message:types.Message):
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp8lMOE92n_uev3ytEoVbB9JT-ejulqmu4uA&s')
    await message.delete()

@router.message(Command('location'))
async def send_locate(message:types.Message):
    await message.answer_location(latitude=55,longitude=74)
    await message.delete()

@router.message(Command('chat_for_man'))
async def start(message:types.Message):
    await message.answer('Только достойные сюда могут зайти...Наверное.Вот ссылка:https://t.me/+Z2q89Tm39Zk0NDRi')
    await message.delete()
@router.message()
async def convert_heart(message:types.Message):
    if message.text == '❤️':
        await message.answer('💔')
