from sqlalchemy import Column, String

from models.base import Base
from models.UserBase import DBUser


def get_data(id, session):
    id = str(id)

    users = session.query(DBUser).all()

    for user in users:
        if user.user_id == id:
            return user.language
    return False