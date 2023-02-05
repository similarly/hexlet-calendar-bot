import requests
import urllib.parse
import datetime
import time
# import json
from calendarbot.src.events_handler import EventsHandler
# from calendarbot.src.calendar import get_events


class Bot:
    KEY = '6040140772:AAF17CAHtCCNgmnf0Wj4ow9DzZJ2bWfFgqQ'

    def __init__(self, service):
        self.service = service

    def set_command(self):
        self.make_request('setMyCommands', commands="[{command: \"/getcalendar}\"]")

    def get_events(self):
        events_handler = EventsHandler(self.service)

        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        print('Getting the upcoming 10 events')

        events_data = events_handler.get_events(calendarId='c_evuik4e31matebv2hn2ahvk05k@group.calendar.google.com',
                                                timeMin=now,
                                                maxResults=30)
        print(events_data[0]["summary"])
        events_text = events_handler.format(events_data, ['summary', 'start'])
        message_text = """*Следующие события:*\n{events}""".format(
            events=events_text)
        self.make_request('sendMessage', chat_id='5000698126',
                          text=message_text, parse_mode='Markdown')

    def start(self):
        # setup
        self.make_request('setMyCommands', commands="""[{"command":"/getcalendar","description":"Get coming Hexlet events."}]""")
        # run
        self.subscribe()

    def subscribe(self):
        offset = 0
        allowed_updates = "[\"message\"]"
        while True:
            url = f"https://api.telegram.org/bot{self.KEY}/getUpdates?offset={offset}&allowedUpdates={allowed_updates}&timeout=60"
            response = requests.get(url, timeout=(3.05, 60))

            # TODO: make it work through make_request function?
            if response.status_code == 200:
                print('succesfully requested updates')
            elif response.status_code != 304:
                print(f"couldn't request updates: {response.status_code}")
                time.sleep(60)
            data = response.json()
            if not data['result']:
                print('NO NEW UPDATES')
            else:
                offset = data['result'][0]['update_id'] + 1
                message_text = data['result'][0]['message']['text']
                if message_text == '/getevents':
                    command = message_text.split(' ')[0]
                    self.get_events()

                # DEBUG
                print(message_text)
                # self.send_message(message_text)
                # print(url)
                time.sleep(1)

    def make_test_request(self):
        self.make_request('sendMessage', chat_id='5000698126',
                          text="SEND BITCHES IT'S TEST REQUEST")

    def make_request(self, methodName, **params):
        print('making request..')
        query = f"{methodName}?{'&'.join([pName + '=' + pValue for pName, pValue in self.escape_query_params(params).items()])}"
        url = f"https://api.telegram.org/bot{self.KEY}/{query}"
        print('sending get request: ' + url)
        response = requests.get(url)
        if response.status_code == 200:
            print('succesfully made request')
        else:
            print(f"couldn't make request error: {response.status_code} ")

    def send_message(self, text: str = "Default message.", chat_id='5000698126', **params):
        params.update(text=text, chat_id=chat_id)
        self.make_request('sendMessage', **params)

    def escape_query_params(self, params: dict) -> dict:
        """Escape query parameters with %XX."""
        return {k: urllib.parse.quote(v, safe='/{}[]:"') for k, v in params.items()}
