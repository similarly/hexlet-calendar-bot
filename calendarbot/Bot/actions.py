from calendarbot.Bot.calendarmodule import CalendarModule
from calendarbot.Bot.botrequests import send_message
from calendarbot.Utils.validators import is_calendar_id, get_args

# This module is responsible for chat commands handling and calling relevant modules.

class Actions:
    commands: dict = {
        '/getevents': 'get_calendar_events',
        '/press': 'press',
        '/subscribe': 'subscribe',
        '/unsubscribe': 'unsubscribe'
    }

    def execute(self, text: str, update: dict) -> None:
        """Execute command from the chat."""
        command = text.split(' ')[0]
        if command in self.commands.keys():
            getattr(self, str(self.commands.get(command)))(update)
        else:
            print('NOT A COMMAND.')

    def get_calendar_events(self, update: dict) -> None:
        """Send events from a calendar to a user."""
        user_id = update['message']['from']['id']
        args = update['message']['text'].split(' ')[1:]
        if len(args) == 0:
            send_message('You need to give calendar URL!', user_id)
            return
        # TODO: Add validation from calendars module ?
        calendar_id = args[0]
        if is_calendar_id(calendar_id):
            calendar = CalendarModule()
            calendar.send_events(user_id, calendar_id)

    def subscribe(self, update: dict) -> None:
        """Subscribe a user to a calendar."""
        user_id = update['message']['from']['id']
        text = update['message']['text']
        try:
            args = get_args(text, amount = 1)
        except Exception:
            send_message('Sorry, wrong arguments!', user_id) 
            return                 
        calendar_id = args[0]
        if is_calendar_id(calendar_id):
            calendar = CalendarModule()
            calendar.subscribe(user_id, calendar_id)
    
    # @calendar_argument decorator ?
    def unsubscribe(self, update: dict) -> None:
        """Unsubscribe a user from a calendar."""
        user_id = update['message']['from']['id']
        text = update['message']['text']
        try:
            args = get_args(text, amount = 1)
        except Exception:
            send_message('Sorry, wrong arguments!', user_id) 
            return
        calendar_id = args[0]
        if is_calendar_id(calendar_id):
            calendar = CalendarModule()
            calendar.unsubscribe(user_id, calendar_id)
        