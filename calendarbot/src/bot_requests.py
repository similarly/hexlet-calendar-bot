import requests
import urllib

def make_request(key, methodName, **params):
    query = f"{methodName}?{'&'.join([pName + '=' + pValue for pName, pValue in _escape_query_params(params).items()])}"
    url = f"https://api.telegram.org/bot{key}/{query}"
    print('Sending telegram API request: ' + url[0:120])
    response = requests.get(url)
    if response.status_code == 200:
        print('Succesfully made request.')
    else:
        print(f"Couldn't make request, error: {response.status_code} ")

def _escape_query_params(params: dict) -> dict:
    """Escape query parameters with %XX."""
    return {k: urllib.parse.quote(v, safe='/{}[]:"') for k, v in params.items()}

def send_message(key, text: str = "Default message.", chat_id='5000698126', **params):
    params.update(text=text, chat_id=chat_id)
    make_request(key, 'sendMessage', **params)