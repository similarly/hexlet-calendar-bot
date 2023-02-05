import requests
import time

from calendarbot.src.calendar import Calendar


class Bot:
    KEY: str = '6040140772:AAF17CAHtCCNgmnf0Wj4ow9DzZJ2bWfFgqQ'

    def start(self) -> None:
        self.subscribe()

    def subscribe(self) -> None:
        """Listens to updates via longpolling."""
        offset = 0
        allowed_updates = "[\"message\"]"
        while True:
            url = f"https://api.telegram.org/bot{self.KEY}/getUpdates?offset={offset}&allowedUpdates={allowed_updates}&timeout=60"
            response = requests.get(url, timeout=(3.05, 60))

            # TODO: make it work through make_request function?
            if response.status_code == 200:
                print('Succesfully requested updates.')
            elif response.status_code != 304:
                print(f"Couldn't request updates: {response.status_code}")
                time.sleep(60)
            data = response.json()
            if not data['result']:
                print('NO NEW UPDATES')
            else:
                offset = data['result'][0]['update_id'] + 1
                if 'text' in data['result'][0]['message'].keys():
                    message_text = data['result'][0]['message']['text']
                    if message_text == '/getcalendar':
                        calendar = Calendar()
                        calendar.send_events()
                    # DEBUG
                    print('MESSAGE: ' + message_text)
                time.sleep(1)
