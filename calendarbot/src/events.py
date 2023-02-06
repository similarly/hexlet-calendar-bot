import datetime
from typing import List
from typing_extensions import Self
from dataclasses import dataclass

@dataclass
class Events:
    """Parses event list returned by the google calendar API."""
    event_list: List[dict]
    
    def __post_init__(self) -> None:
        """Separates event summary into event description (summary) and event host (lecturer), and formats start time."""
        for event in self.event_list:
            # Create new fields
            split = event['summary'].split(';')
            # If no author
            if len(split) == 1:
                body = split
                after_semi = 'Нет наставника.'
            else:
                body = ';'.join(split[0:-1])
                after_semi = split[-1]
            # Format start time
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_formatted = datetime.datetime.fromisoformat(
                start).strftime("%d.%m, %H:%M")
            event.update({'start': start_formatted, 'summary': body, 'author': after_semi})
        
    def _get_dict(self) -> dict:
        """Return dictionary contained inside class instance."""
        return self.event_list

    def format(self, keys: List[str]) -> str:
        blocks_list = []
        for event in self._get_dict():
            # DEBUG
            print('• ' + event.get('summary', '- no summary -'))
            # Join event dictionary keys into block
            block = '\n'.join([event.get(key).strip() for key in keys])
            blocks_list.append('• ' + block + '\n')
        formatted_events = ''.join(blocks_list)
        return formatted_events

    def has_author(self) -> Self:
        bad_cases = [' Наставник', 'Наставник',
                     ' (ФИ наставника)', '(ФИ наставника)', ' (ФИ наставника) ', 'Нет наставника']
        # TODO: Add dunder methods later so class instances could be iter'd outside of class
        filtered_events = [event for event in self._get_dict(
        ) if event.get('author') not in bad_cases]
        return Events(filtered_events)