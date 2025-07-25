from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable, Union
from DB.requests import checkgoogle
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class AuthMiddleware(BaseMiddleware):
    ACTIONS = ("/create_form", "/my_forms", "/stats", "создать Форму", "мои Формы", "статистика")

    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message) and event.text:
            text = event.text.strip().lower()
            if not any(text.startswith(action) for action in self.ACTIONS):
                return await handler(event, data)
        else:
            return await handler(event, data)
        
        user_id = event.from_user.id
        auth_status = await checkgoogle(user_id)

        if auth_status == "valid":
            return await handler(event, data)
        if auth_status == "no_account":
            await self.send_authmess(event)
        elif auth_status == "expired":
            return
        return
    
    
    async def send_authmess(self, message: Message):
        await message.answer("Вы не авторизованы\nДля авторизации, перейдите по кнопке ниже:",
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(
                text="Авторизоваться через мини-приложение",
                url="https://t.me/GoogleForm_NTT_bot/GFNapstasAUTHAPP"  # Замените на реальный URL
            )]
        ]))