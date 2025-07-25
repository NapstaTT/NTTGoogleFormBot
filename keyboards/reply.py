from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MKB = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Создать Форму')],
                                    [KeyboardButton(text='Мои Формы')],
                                    [KeyboardButton(text='Статистика')],
                                    [KeyboardButton(text='Помощь')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите пункт меню...')


FMKB = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Получить Ссылку')],
                                    [KeyboardButton(text='Добавить Вопрос')],
                                    [KeyboardButton(text='Удалить')],
                                    [KeyboardButton(text='Статистика')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите действие с формой')


SKB = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Диаграмма')],
                                    [KeyboardButton(text='Текст')],
                                    [KeyboardButton(text='CSV')],
                                    [KeyboardButton(text='Помощь')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите пункт меню...')