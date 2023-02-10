from __future__ import print_function

import datetime

from calendarbot.Bot.botrequests import send_message
from calendarbot.Bot.events import Events
from calendarbot.Bot.googleauth import GoogleAuth
from calendarbot.config import Config

from calendarbot.Models.calendar import Calendar
from calendarbot.Models.user import User
from calendarbot import Session

# This module is responsible for working with Calendars

class CalendarModule:
    KEY: str = Config.telegram_API_key

    def __init__(self) -> None:
        self.service = GoogleAuth.get_service()

    def subscribe(self, user_id: str, calendar_id: str) -> None:
        session = Session()
        user_id_int = int(user_id)
        user = session.query(User).filter(User.telegram_id == user_id_int).first()
        calendar = session.query(Calendar).filter(Calendar.calendar_id == calendar_id).first()
        # TODO: Refactor and use those id's as Primary keys and use try, except and conflict exception
        # If no user or calendar in database
        if not user:
            user = User(user_id_int)
        if not calendar:
            calendar = Calendar(calendar_id)
        user.calendars.append(calendar)
        session.add(user)
        session.commit()
        print(f'Subscribed user {user_id} to calendar {calendar_id}')
        pass
    
    def unsubscribe(self, user_id: str, calendar_id: str) -> None:
        pass

    def send_events(self, user_id: str, calendar_id: str) -> None:
        # Get events
        print('Getting events..')
        events = self._get_events(calendar_id).format(
            ['summary', 'start', 'author'])
        # Format message
        message_text = """*Следующие события:*\n{events}""".format(
            events=events)
        # Send message
        send_message(message_text,
                     user_id, parse_mode='Markdown')

    def _get_events(self, calendar_id: str) -> Events:
        # Get current time
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # Call API
        events = Events(self.service.events().list(calendarId=calendar_id,
                                                   timeMin=now,
                                                   maxResults=7,
                                                   orderBy='startTime',
                                                   singleEvents=True).execute().get('items', []))
        print("Got events.")
        if not events:
            print('No upcoming events found.')
            return Events([])
        return events
