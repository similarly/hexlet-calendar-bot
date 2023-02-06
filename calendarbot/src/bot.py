import requests
import time

from calendarbot.src.updates import Updates
from calendarbot.src.actions import Actions
from calendarbot.src.config import APIkeys

class Bot:
    KEY: str = APIkeys.telegramAPIKey
    
    def start(self) -> None:
        self.subscribe()

    def subscribe(self) -> None:
        """Listens to updates via longpolling."""
        offset = 0
        allowed_updates = "[\"message\"]"
        while True:
            url = f"https://api.telegram.org/bot{self.KEY}/getUpdates?offset={offset}&allowedUpdates={allowed_updates}&timeout=60"
            response = requests.get(url, timeout=(3.05, 60))
            if response.status_code == 200:
                print('Succesfully requested updates.')
            elif response.status_code != 304:
                print(f"Couldn't request updates: {response.status_code}")
                time.sleep(60)
            updates = Updates(response.json()['result'])
            if updates.is_empty():
                print('NO NEW UPDATES')
            else:
                # TODO Get and process updates in batches
                update = updates[0]
                offset = update.get('update_id') + 1
                try:
                    text = update.get('message').get('text')
                    if not text:
                        raise Exception('NO MESSAGE UPDATE.')
                    print('MESSAGE: ' + text)
                    if text[0] == '/':
                        action = Actions()
                        action.execute(text)
                except Exception as e:
                    print(e)
                    pass
                # time.sleep(1)