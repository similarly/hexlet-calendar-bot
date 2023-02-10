from sqlalchemy import Column, Integer,  BigInteger
from sqlalchemy.orm import relationship

from calendarbot import Base
from calendarbot.Models.calendar import users_calendars_association

class User(Base):
    # Map rows of users to class Users
    __tablename__ = 'users'
    
    # Columns
    id = Column(Integer, primary_key=True)
    telegram_id = Column('telegram_id', BigInteger, unique=True)

    # Relationship, calendar has backref
    # TODO: make it explicit with back_populates=""
    # calendars = relationship("Calendar", secondary=users_calendars_association)
    
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id