from calendarbot.Models.calendar import Calendar
from calendarbot.Models.user import User
from calendarbot import Base, Session, engine

Base.metadata.create_all(engine)
session = Session()

# Creating users
user_vasya = User(3423452)
user_petya = User(999999)

# Creating calendars and relationships

calendar_hexlet = Calendar('c_evuik4e31matebv2hn2ahvk05k@group.calendar.google.com')
calendar_jewish = Calendar('ru.judaism#holiday@group.v.calendar.google.com')
calendar_christian = Calendar('ru.christian#holiday@group.v.calendar.google.com')

user_vasya.calendars = [calendar_hexlet, calendar_jewish, calendar_christian]
user_petya.calendars = [calendar_hexlet]

# Session add
session.add(user_vasya)
session.add(user_petya)

# Commit and close
session.commit()
session.close()