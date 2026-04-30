from sqlalchemy import Column, BigInteger, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"
    id: Column(BigInteger, primary_key=True)
    title: Column(String(255))
    content: Column(Text)