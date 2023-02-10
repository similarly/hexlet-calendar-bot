from sqlalchemy import Column, Integer

from calendarbot import Base


class User:
    # Map rows of users to class Users
    __tablename__ = 'users'
    # Columns
    id = Column(Integer, primary_key=True)
    telegram_id = Column('telegram_id', Integer)
