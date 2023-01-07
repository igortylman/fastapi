from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# below imports are not being used currently
import psycopg2
from psycopg2.extras import RealDictCursor
import time

sqlalchemy_database_url = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# code below is not being used since I started using sqlalchemy to talk to postgres.
# it is there just for documentation purposes
"""
while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password='gV12uip100', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successful')
        break
    except Exception as error:
        print('Connection to database failed')
        print("Error:", error)
        time.sleep(2)
"""

