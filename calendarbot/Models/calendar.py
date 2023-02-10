from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from calendarbot import Base

# Pivot table
users_calendars_association = Table(
    'users_calendars', Base.metadata,
    Column('calendar_id', ForeignKey('calendars.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True)
)

class Calendar(Base):
    # Map rows of users to class Users
    __tablename__ = 'calendars'
    
    # Columns
    # TODO: calendar_name=Column(Integer, foreign_key=True)
    id = Column(Integer, primary_key=True)
    calendar_id = Column('calendar_id', String)
    
    # Relationships
    users = relationship("User", secondary=users_calendars_association, backref="calendars")

    def __init__(self, calendar_id):
        self.calendar_id = calendar_id