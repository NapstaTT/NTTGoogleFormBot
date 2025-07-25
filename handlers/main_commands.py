from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards import reply as rkb
from BD import requests as rq

router = Router()

help_message='''
/start - начало работы
/help - вывести список команд
/description - описание бота
'''


@router.message(Command('start'))
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.username)
    await message.answer(
        text="Добро пожаловать в бот для менеджмента Google Forms!",
        reply_markup=rkb.MKB
    )
    await message.delete()


@router.message(F.text == 'Помощь' or '/help')
async def cmd_help(message: Message):
    await message.answer(help_message)
    await message.delete()

@router.message(F.text == 'Мои формы' or '/my_forms')
async def myforms(mesage: Message):
    pass

@router.message(F.text == 'Статистика' or '/stats')
async def statsofform(mesage: Message):
    pass
