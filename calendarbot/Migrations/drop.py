from sqlalchemy import MetaData

from calendarbot import Base, Session, engine
from calendarbot.Models.calendar import Calendar
from calendarbot.Models.user import User

session = Session()

tables_to_drop = ['users_calendars', 'calendars', 'users']

def drop_tables(tables: list):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    for table in tables:
        try:
            table = metadata.tables[table]
        except KeyError:
            continue
        if table is not None:
            Base.metadata.drop_all(engine, [table], checkfirst = True)
    print('TABLES DROPPED.')

# Could do:
# session.query(User).delete()

session.commit()

if __name__ == '__main__':
    drop_tables(tables_to_drop)
