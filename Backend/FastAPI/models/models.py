from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from pydantic import BaseModel


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    surname: Mapped[str] = mapped_column(String(255))
    age: Mapped[int]
    subscribers: Mapped[int]
    subscriptions: Mapped[int]
    posts: Mapped[int]
    likes: Mapped[int]
    refresh_token: Mapped[str] = mapped_column(String(255))


class Posts(Base):
    __tablename__ = 'posts'

    user_id: Mapped[int]
    id: Mapped[int] = mapped_column(primary_key=True)
    likes: Mapped[int]
    content: Mapped[str] = mapped_column(String(535))


class Subs(Base):
    __tablename__ = "subs"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int]
    child_id: Mapped[int]

