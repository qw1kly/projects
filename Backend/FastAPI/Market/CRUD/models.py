from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    uuid: Mapped[str | None] = mapped_column(String(55))
    name: Mapped[str] = mapped_column(String(105))
    login: Mapped[str] = mapped_column(String(105), unique=True)
    password: Mapped[str] = mapped_column(String(105))


class Items(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    name: Mapped[str] = mapped_column(String(105))
    weight: Mapped[int]
    price: Mapped[int]


class Admin(Base):
    __tablename__ = "admins"

    uuid: Mapped[str | None] = mapped_column(String(55))
