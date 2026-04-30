from sqlalchemy import Column, BigInteger, String, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"
    id: Column(BigInteger, primary_key=True)
    title: Column(String(255))
    content: Column(Text)