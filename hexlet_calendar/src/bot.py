import requests
import urllib.parse

KEY = '6040140772:AAF17CAHtCCNgmnf0Wj4ow9DzZJ2bWfFgqQ'


def make_test_request():
    make_request('sendMessage', chat_id='5000698126',
                 text="SEND BITCHES IT'S TEST REQUEST")


def make_request(methodName, **params):
    print('making request..')
    query = f"{methodName}?{'&'.join([pName + '=' + pValue for pName, pValue in parse_params(params).items()])}"
    URL = f"https://api.telegram.org/bot{KEY}/{query}"
    print(URL)
    r = requests.get(URL)
    if r.status_code == 200:
        print('succesful!')
    else:
        print('error:')
        print(r.status_code)


def send_message(**params):
    make_request('sendMessage', **params)

def parse_params(params):
    return {k: urllib.parse.quote(v) for k, v in params.items()}
