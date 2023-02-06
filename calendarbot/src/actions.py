from calendarbot.src.calendar import Calendar
from calendarbot.src.bot_requests import send_message

class Actions:
    commands: dict = {
        "/getcalendar": 'get_calendar',
        "/press": 'press',
    }
    
    def execute(self, text: str) -> None:
        if text in self.commands.keys():
            getattr(self, self.commands.get(text))()
        else:
            print('NOT A COMMAND.') 
        # elif text == '/getcalendar':
            # self.cmd_send_events()
    
    def get_calendar(self):
        calendar = Calendar()
        calendar.send_events()
        
    def press(self):
        send_message('hello!')