from datetime import datetime

from sqlalchemy import Column, BigInteger, String, Text, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(String(5000))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.CURRENT_TIMESTAMP())
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    daily_id: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.CURRENT_TIMESTAMP())