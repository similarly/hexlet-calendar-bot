import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())
@dataclass(frozen=True)
class APIkeys:
    telegramAPIKey: str = os.getenv('telegramAPIKey')