from calendarbot.Bot.calendarmodule import CalendarModule

def is_calendar_id(calendar_id):
    try:
        calendar = CalendarModule()
        # TODO: Think about what could be here instead.
        calendar._get_events(calendar_id)
        return True
    except:
        return False
    
def get_args(message: str, amount: int = 1):
    args = message.split(' ')[1:]
    if len(args) < amount:
        raise Exception('Not enough arguments.')
    return args