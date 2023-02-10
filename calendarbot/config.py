import os
import json
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())

@dataclass(frozen=True)
class Config:
    telegram_API_key: str = os.getenv('telegram_API_key') or ''
    DB_password: str = os.getenv('DB_password') or ''
    DB_username: str = os.getenv('DB_username') or ''
    scopes: str = os.getenv('scopes')# type:    ignore