from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.models import User
from models.UserBase import DBUser

def add_user(user: User, session):
    db_user = DBUser(user_id=user.user_id, language=user.language)
    session.add(db_user)
    session.commit()
    print(f"User {user.user_id} added successfully")

