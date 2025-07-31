from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    title = State()
    sureT = State()