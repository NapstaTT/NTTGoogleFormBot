from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from FSM.states import UserStates
from keyboards.inline import confirm_title_keyboard, type_of_choice_keyboard, type_of_question_keyboard, confirm_choice_keyboard, confirm_question_keyboard, confirm_Q_keyboard
crouter = Router()


@crouter.message(F.text == 'Создать форму' or '/create_form')
async def creation_of_form(message: Message, state: FSMContext):
    await ReplyKeyboardRemove() 
    await state.set_state(UserStates.settitle)
    await message.answer("Для создания формы, пожалуйста, укажите её название следующим сообщением")
    await state.update_data(settitle=message.text)
    await state.set_state(UserStates.sure)
    await message.delete()
@crouter.message(UserStates.sure)
async def sure(message: Message, state: FSMContext):
    await message.reply("Вы уверены, что форма будет названа {UserStates.settitle}?", reply_markup=confirm_title_keyboard)
@crouter.message(F.data=='title_cancel')
async def notsure(message: Message, state: FSMContext):
    await message.delete()
    await creation_of_form()

#cоздание формы типо тут должно быть реализовано, далее уже для update form

def gettypename(type):
    if type=="textQuestion":
        return "Краткий ответ"
@crouter.message(F.data == 'title_confirm')
async def Qtitle(message: Message, state: FSMContext):
    await message.answer("Далее выберите тип вопроса", reply_markup=type_of_question_keyboard)
    await state.set_state(UserStates.settypeofquestion)

@crouter.message(F.data == 'textQuestion')
async def Qcontain(message: Message, state: FSMContext):
    await state.update_data(settypeofquestion="textQuestion")
    await state.set_state(UserStates.setquestiontitle)
    await message.answer("введите текст вопроса:")
    await state.update_data(setquestiontitle=message.text)
    await state.set_state(UserStates.sureQ)

@crouter.message(UserStates.sureQ)
async def SureQuestion(message:Message, state: FSMContext):
    N=gettypename(UserStates.settypeofquestion)
    await message.answer(text = "Подтвердите создание следующего вопроса: \n{UserStates.setquestiontitle}\n, тип вопроса: {N}?", reply_markup=confirm_Q_keyboard )