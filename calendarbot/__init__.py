from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from calendarbot.config import Config

username, password = Config.DB_username, Config.DB_password
engine = create_engine('postgresql://{username}:{password}@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)
Base = declarative_base()

print('DB session maker created..')