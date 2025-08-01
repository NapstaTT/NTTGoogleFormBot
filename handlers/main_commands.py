from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards import reply as rkb
from DB import requests as rq

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


@router.message('/help')
async def cmd_help(message: Message):
    await message.delete()
    await message.answer(help_message)

@router.message(Command('my_forms'))
async def myforms(mesage: Message):
    pass

@router.message(Command('stats'))
async def statsofform(mesage: Message):
    pass
