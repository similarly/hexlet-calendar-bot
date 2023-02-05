import datetime


class EventsHandler:
    def __init__(self, service):
        self.service = service

    def get_events(self, **kwargs) -> list:
        print('Getting events...')
        events_result = self.service.events().list(**kwargs).execute()
        events = events_result.get('items', [])
        if not 'time' not in kwargs.keys():
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            kwargs.time = now

        if not events:
            print('No upcoming events found.')
            return
        events_data = []
        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_formatted = datetime.datetime.fromisoformat(
                start).strftime("%m/%d/%Y, %H:%M:%S")
            events_data.append(
                {'start': start_formatted, 'summary': event['summary']})
        return events_data

    def format(self, events_data: list, keys: list) -> str:
        blocks_list = []
        for event in events_data:
            block = '\n'.join([event.get(key) for key in keys])
            blocks_list.append('• ' + block + '\n')
        formatted_events = ''.join(blocks_list)
        # formatted_events = '\n'.join([f"• {event.get('summary')}\n{event.get('start')}" for event in events_data])
        return formatted_events
