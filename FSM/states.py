from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    title = State() #работа с названием формы
    sureT = State() #подтверждения названия формы
    questionTi = State() #работа с вопросом
    questionTy = State() #работа с типом вопроса
    sureQ = State() #подтверждение создания вопроса