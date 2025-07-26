from sqlalchemy import Column, String

from models.base import Base

class DBUser(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True)
    language = Column(String)
