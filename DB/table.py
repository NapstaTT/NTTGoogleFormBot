from datetime import datetime, timezone
from sqlalchemy import BOOLEAN, BigInteger, TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[BigInteger] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, 
        default=lambda: datetime.now(timezone.utc)
    )
    
    # Обратная связь 1:1 к GoogleAccount
    google_account: Mapped["GoogleAccount"] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )
    
    # Обратная связь 1:ко-многим к формам
    forms: Mapped[list["FormMeta"]] = relationship(
        back_populates="owner",
        cascade="all, delete"
    )

class GoogleAccount(Base):
    __tablename__ = 'google_accounts'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(ForeignKey('users.tg_id'))
    google_email: Mapped[str] = mapped_column(String(50))
    access_token: Mapped[str] = mapped_column(String(500))
    refresh_token: Mapped[str] = mapped_column(String(500))
    expires_at: Mapped[datetime] = mapped_column(datetime)

    # Обратная связь 1:1 к User
    user: Mapped["User"] = relationship(
        back_populates="google_account"
    )
    
    # Обратная связь 1:ко-многим к формам
    forms: Mapped[list["FormMeta"]] = relationship(
        back_populates="google_account"
    )

class FormMeta(Base):
    __tablename__ = 'forms_meta'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    google_account_id: Mapped[int] = mapped_column(ForeignKey('google_accounts.id'))
    google_form_id: Mapped[str] = mapped_column(String(150))
    title: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, 
        default=lambda: datetime.now(timezone.utc)
    )
    is_active: Mapped[bool] = mapped_column(BOOLEAN, default=True)

    # Обратная связь многие:к-1 к GoogleAccount
    google_account: Mapped["GoogleAccount"] = relationship(
        back_populates="forms"
    )
    
    # Обратная связь многие:к-1 к User (через GoogleAccount)
    owner: Mapped["User"] = relationship(
        back_populates="forms",
        viewonly=True,
        overlaps="google_account, forms"
    )