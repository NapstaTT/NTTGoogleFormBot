from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_title_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data="title_confirm"),
            InlineKeyboardButton(text="❌ Отменить", callback_data="title_cancel")
        ]
    ])
def confirm_Q_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data="Q_confirm"),
            InlineKeyboardButton(text="❌ Отменить", callback_data="Q_cancel")
        ]
    ])
def type_of_question_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Текстовый Ответ", callback_data="textQuestion"),
            InlineKeyboardButton(text="Значение на шкале", callback_data="scaleQuestion"),
            InlineKeyboardButton(text="Выбор из вариантов", callback_data="choiceQuestion")
        ]
    ])
def type_of_choice_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Один вариант", callback_data="RADIO"),
            InlineKeyboardButton(text="Несколько вариантов", callback_data="CHECKBOX"),
            InlineKeyboardButton(text="Выпадающий список", callback_data="DROP_DOWN")
        ]
    ])
def confirm_question_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data="title_confirm"),
            InlineKeyboardButton(text="❌ Создать заново", callback_data="title_cancel")
        ]
    ])

def confirm_option_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data="title_confirm"),
            InlineKeyboardButton(text="❌ Отменить", callback_data="title_cancel")
        ]
    ])