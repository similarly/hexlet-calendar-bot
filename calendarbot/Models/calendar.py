from sqlalchemy import Column, Integer

from calendarbot import Base


class Calendar:
    # Map rows of users to class Users
    __tablename__ = 'calendars'
    # Columns
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, foreign_key=True)
    # Like c_evuik4e31matebv2hn2ahvk05k@group.calendar.google.com
    calendar_id = Column('telegram_id', Integer)
    # TODO: calendar_name=Column(Integer, foreign_key=True)
