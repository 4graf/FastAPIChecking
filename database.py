import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import as_declarative

log = logging.getLogger(__name__)

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_BASE_URL = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/'
DB_FULL_URL = DB_BASE_URL + DB_NAME


try:
    base_engine = create_engine(DB_BASE_URL)
    with base_engine.connect() as conn:
        conn.execute(text('commit'))
        create_db_query = text(f'CREATE DATABASE {DB_NAME};')  # when using the parameterized query quotes are added
        # to the string
        conn.execute(create_db_query)

        logging.info(f'Database {DB_NAME} created. Create session')
except ProgrammingError as exc:
    if 'DuplicateDatabase' in exc.args[0]:  # check psycopg2 error
        logging.info(f'Database {DB_NAME} exist. Create session')
    else:
        logging.critical(exc, exc_info=True)
        raise exc
except Exception as exc:
    logging.critical(exc, exc_info=True)
    raise exc

engine = create_engine(DB_FULL_URL)
Session = sessionmaker(bind=engine)


@as_declarative()
class Base:
    pass


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
