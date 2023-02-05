import requests
import urllib.parse
import datetime
from hexlet_calendar.src.events_handler import EventsHandler

KEY = '6040140772:AAF17CAHtCCNgmnf0Wj4ow9DzZJ2bWfFgqQ'

class Bot:
    def __init__(self, service):
        self.service = service

    def start_bot(self):
        events_handler = EventsHandler(self.service)
        
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        print('Getting the upcoming 10 events')

        events_data = events_handler.get_events(calendarId='c_evuik4e31matebv2hn2ahvk05k@group.calendar.google.com',
                                                timeMin=now,
                                                maxResults=30)
        print(events_data[0]["summary"])
        events_text = events_handler.format(events_data, ['summary', 'start'])
        # events_list_text = '\n'.join([f"• {event.get('summary')}\n{event.get('start')}" for event in events_data])
        message_text = """*Следующие события:*\n{events}""".format(
            events=events_text)
        self.make_request('sendMessage', chat_id='5000698126',
                        text=message_text, parse_mode='Markdown')

    def make_test_request(self):
        self.make_request('sendMessage', chat_id='5000698126',
                    text="SEND BITCHES IT'S TEST REQUEST")


    def make_request(self, methodName, **params):
        print('making request..')
        query = f"{methodName}?{'&'.join([pName + '=' + pValue for pName, pValue in self.parse_params(params).items()])}"
        URL = f"https://api.telegram.org/bot{KEY}/{query}"
        print(URL)
        r = requests.get(URL)
        if r.status_code == 200:
            print('succesful!')
        else:
            print('error:')
            print(r.status_code)


    def send_message(self, **params):
        self.make_request('sendMessage', **params)

    def parse_params(self, params):
        return {k: urllib.parse.quote(v) for k, v in params.items()}
