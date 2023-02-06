from __future__ import print_function

import os.path
import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

from calendarbot.src.bot_requests import send_message
from calendarbot.src.events import Events 


class Calendar:
    # If modifying these scopes, delete the file token.json.
    SCOPES: str = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    KEY: str = '6040140772:AAF17CAHtCCNgmnf0Wj4ow9DzZJ2bWfFgqQ'
    CHAT_ID: str = '5000698126'
    CALENDAR_ID: str = 'c_evuik4e31matebv2hn2ahvk05k@group.calendar.google.com'

    def __init__(self) -> None:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file(
                'token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        try:
            self.service = build('calendar', 'v3', credentials=creds)
        except HttpError as error:
            print('An error occurred: %s' % error)

    def get_events(self) -> list:
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting events...')
        # Call API
        events = self.service.events().list(calendarId=self.CALENDAR_ID,
                                                     timeMin=now,
                                                     maxResults=7,
                                                     orderBy='startTime',
                                                     singleEvents=True).execute().get('items', [])
        print("Got 'em")
        if not events:
            print('No upcoming events found.')
            return
        return events

    def send_events(self) -> None:
        events = Events(self.get_events()).format(['summary', 'start', 'author'])
        message_text = """*Следующие события:*\n{events}""".format(
            events=events)
        # Send message
        send_message(self.KEY, text=message_text,
                     chat_id=self.CHAT_ID, parse_mode='Markdown')