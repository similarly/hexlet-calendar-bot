import requests

from time import sleep
from calendarbot.Bot.updates import Updates
from calendarbot.Bot.actions import Actions
from calendarbot.config import Config


class Bot:
    KEY: str = Config.telegram_API_key

    def start(self) -> None:
        self.subscribe()

    def subscribe(self) -> None:
        """Listens to updates via longpolling."""
        offset = 0
        allowed_updates = "[\"message\"]"
        while True:
            try:
                url = f"https://api.telegram.org/bot{self.KEY}/getUpdates?offset={offset}&allowedUpdates={allowed_updates}&timeout=60"
                response = requests.get(url, timeout=(3.05, 60))
            except Exception as e:
                print('Exception occured: ', e)
                sleep(5)
                continue

            # TODO Get and process updates in batches
            updates = Updates(response.json().get('result'))
            if updates.is_empty():
                print('NO NEW UPDATES')
                continue
            update = updates[0]
            offset = update['update_id'] + 1
            try:
                text = update['message']['text']
                if not text:
                    raise Exception('NOT A MESSAGE UPDATE.')
                print('MESSAGE: ' + text)
                if text[0] == '/':
                    action = Actions()
                    action.execute(text, update)
            except Exception as e:
                print('Exception occured: ', e)
