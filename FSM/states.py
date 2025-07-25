from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    main_menu = State()
    myforms = State()
    statistics = State()

#createform:
    settitle = State()
    setquestiontitle = State()
    settypeofquestion = State()
    question = State()
    option = State()
    sure = State()
    sureQ = State()

    choosingformtoredact = State()
    choosingformforstats = State()
