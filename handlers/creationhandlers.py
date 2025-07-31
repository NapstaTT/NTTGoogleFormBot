from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from keyboards.inline import confirm_title_keyboard

from FSM.states import UserStates
crouter = Router()


@crouter.message(F.text == 'Создать форму' or '/create_form')
async def creation_of_form(message: Message, state: FSMContext):
    await ReplyKeyboardRemove() 
    await state.set_state(UserStates.title)
    await message.reply("Для создания формы, пожалуйста, укажите её название")

@crouter.message(StateFilter(UserStates.title))
async def settingTitle(message: Message, state: FSMContext):
    await state.update_data(title = message.answer)
    await state.set_state(UserStates.sureT)

@crouter.message(StateFilter(UserStates.sureT))
async def suretitle(message: Message, state: FSMContext):
    data=await state.get_data
    await message.reply(f"Вы уверены, что форма будет названа {data.title}?", reply_markup=confirm_title_keyboard)

@crouter.callback_query(F.data == "title_cancel")
async def wrongT(message: Message, state: FSMContext, callback: CallbackQuery):
    await state.set_state(UserStates.title)
    await callback.answer("Для создания формы, пожалуйста, укажите её название")

@crouter.callback_query(F.data == "title_confirm")
async def corrT(message: Message, state: FSMContext, callback: CallbackQuery):
    pass