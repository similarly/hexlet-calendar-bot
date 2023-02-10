import requests
from urllib import parse
from calendarbot.config import Config

def make_request(methodName, **params):
    KEY: str = Config.telegram_API_key
    query = f"{methodName}?{'&'.join([pName + '=' + pValue for pName, pValue in _escape_query_params(params).items()])}"
    url = f"https://api.telegram.org/bot{KEY}/{query}"
    print('Sending telegram API request: ' + url[0:120])
    response = requests.get(url)
    if response.status_code == 200:
        print('Succesful request to telegram API.')
    else:
        print(f"Couldn't make request to telegram API, error: {response.status_code} ")

def _escape_query_params(params: dict) -> dict:
    """Escape query parameters with %XX."""
    return {k: parse.quote(str(v), safe='/{}[]:"') for k, v in params.items()}

def send_message(text: str = "Default message.", chat_id='5000698126', **params):
    params.update(text=text, chat_id=chat_id)
    make_request('sendMessage', **params)