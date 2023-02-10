from calendarbot.Bot.calendar import Calendar
from calendarbot.Bot.botrequests import send_message


class Actions:
    commands: dict = {
        "/getcalendar": 'get_calendar',
        "/press": 'press',
        "/subscribe": 'subscribe',
    }

    def execute(self, text: str, payload: dict = {}) -> None:
        if text in self.commands.keys():
            getattr(self, str(self.commands.get(text)))(payload)
        else:
            print('NOT A COMMAND.')

    def get_calendar(self, payload):
        calendar = Calendar()
        calendar.send_events(payload)

    def press(self, payload):
        name = payload['message']['chat']['first_name']
        chat_id = payload['message']['from']['id']
        send_message(f'hello!, your username is {name}', chat_id)
