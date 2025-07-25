from table import User, GoogleAccount, FormMeta
from core import async_session
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone

async def set_user(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            session.add(User(username=username))
            await session.commit()

async def checkgoogle(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User)
                                    .where(User.tg_id==tg_id)
                                    .options(selectinload(User.google_account)))
        if not user.google_account:
            return "no_google_account"
        current_time=datetime.now(timezone.utc)
        if user.google_account.expires_at<current_time:
            return "token_expired"
        else:
            return "valid"
