from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from keyboards.inline import confirm_title_keyboard, confirm_Q_keyboard, finish_form

from FSM.states import UserStates
crouter = Router()


@crouter.message(F.text == 'Создать форму')
async def creation_of_form(message: Message, state: FSMContext): #Запрос названия формы
    await ReplyKeyboardRemove() 
    await state.set_state(UserStates.title)
    await message.reply("Для создания формы, пожалуйста, укажите её название")

@crouter.message(StateFilter(UserStates.title))
async def settingTitle(message: Message, state: FSMContext): #Обработка названия формы
    await state.update_data(title = message.text)
    await state.set_state(UserStates.sureT)

@crouter.message(StateFilter(UserStates.sureT))
async def suretitle(message: Message, state: FSMContext): #Запрос подтверждения указаного названия
    data=await state.get_data()
    data=data.get("title")
    await message.reply(f"Вы уверены, что форма будет названа {data}?", reply_markup=confirm_title_keyboard)

@crouter.callback_query(F.data == "title_cancel") 
async def wrongT(callback: CallbackQuery, state: FSMContext):#Обработка отказа 
    await state.set_state(UserStates.title)
    await callback.answer("Для создания формы, пожалуйста, укажите её название")

@crouter.callback_query(F.data == "title_confirm")
async def corrT(callback: CallbackQuery, state: FSMContext): #Обработка подтверждения
    await callback.message.answer("Форма успешно создана, теперь введите формулировку первого вопроса")
    await state.set_state(UserStates.questionTi)
    await state.update_data(questionTi=[], questionTy=[], index=0) #инициализация списка вопросов

@crouter.message(StateFilter(UserStates.questionTi))
async def settingQ(message: Message, state: FSMContext): #Обработка названия вопроса
    data = await state.get_data()
    questionTi_list = data.get("questionTi")
    new_questionTi = questionTi_list + [message.text]
    await state.update_data(
        questionTi=new_questionTi
    )
    await state.set_state(UserStates.questionTy)
    await message.answer("Теперь выберите тип вопроса: доступен пока только с расширенным ответом")

@crouter.message(StateFilter(UserStates.questionTy))
async def settingT(message: Message, state: FSMContext): #Обработка типа вопроса
    data = await state.get_data()
    questionTy_list = data.get("questionTy")
    new_questionTy = questionTy_list + ["textQuestion"]
    await state.update_data(
        questionTy=new_questionTy
    )
    await state.set_state(UserStates.sureQ)
    question_titles = data["questionTi"]
    current_index = data["index"]
    last_question_index = current_index
    question_title = question_titles[last_question_index]
    question_type = new_questionTy[last_question_index]
    await message.reply(
        f"Подтвердите создание вопроса:\n\n"
        f"📝 Название: {question_title}\n"
        f"🔧 Тип: {question_type}",
        reply_markup=confirm_Q_keyboard
    )

@crouter.callback_query(F.data == "FCANCEL")
async def formcancel(callback: CallbackQuery, state: FSMContext): #Обработка отмены создания формы
    await callback.message.answer("Вы отменили создание формы")
    await state.clear()

@crouter.callback_query(F.data == "Q_cancel")
async def Qcancel(callback: CallbackQuery, state: FSMContext): #Обработка отмены текущего вопроса
    data = await state.get_data()
    new_questionTi = data["questionTi"][:-1]
    new_questionTy = data["questionTy"][:-1]
    await state.update_data(
        questionTi=new_questionTi,
        questionTy=new_questionTy
    )
    await callback.message.answer("Вопрос удалён, введите новую формулировку вопроса")
    await state.set_state(UserStates.questionTi)

@crouter.callback_query(F.data == "Q_confirm")
async def Qconfirm(callback: CallbackQuery, state: FSMContext): #Обработка отмены текущего вопроса
    data = await state.get_data()
    new_index = data["index"]+1
    await state.update_data(
        index=str(new_index)
    )
    await callback.message.answer("Вопрос успешно сохранён, введите формулировку нового вопроса или нажмите на кнопку ниже для завершения создания формы", reply_markup=finish_form)
    await state.set_state(UserStates.questionTi)
@crouter.callback_query(F.data == "finishF")
async def finishF(callback: CallbackQuery, state: FSMContext):
    #тут будет вызван метод для отправки HTTP запроса в гугл с данным, с аргументом в виде другого метода для формирования payload
    await state.clear()
    await callback.message.answer("Форма успешно создана~")